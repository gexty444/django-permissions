from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, View

from ..decorators import planner_required, finalisation_required
from ..forms import PlannerSignUpForm
from ..models import User

usertypes = { 
    'professor': 1, 
    'eventplanners': 2, 
    'coursecoordinators': 3, 
    'timetableplanner': 4, 
    'student' : 5
}

class PlannerSignUpView(CreateView):
    model = User
    form_class = PlannerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'planner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        userdetail = form.save(commit=False)
        try:
            userdetail.phase = User.objects.filter(user_type=usertypes['professor'])[0].phase
        except:
            userdetail.phase = 1
        userdetail = form.save()
        login(self.request, userdetail)
        return redirect('planners:planner_main')


@method_decorator([login_required, planner_required], name='dispatch')
class PlannerMainView(TemplateView):
    template_name = 'users/planners/planner_main.html'



@method_decorator([login_required, planner_required], name='dispatch')
class CurrentPhase(TemplateView):
    template_name = 'users/planners/planner_currentphase.html'


@method_decorator([login_required, planner_required], name='dispatch')
class NextPhase(View):

    def get(self, request, *args, **kwargs):
        current_phase = self.request.user.phase
        # change phase to next phase
        if (current_phase < 3):
            User.objects.all().update(phase=current_phase+1)
        # to reset
        # User.objects.all().update(phase=1)
        return redirect('planners:currentphase')

@method_decorator([login_required, planner_required], name='dispatch')
class PreviousPhase(View):

    def get(self, request, *args, **kwargs):
        current_phase = self.request.user.phase
        # change phase to previous phase
        if (current_phase > 1 ):
            User.objects.all().update(phase=current_phase-1)
        # to reset
        # User.objects.all().update(phase=1)
        return redirect('planners:currentphase')

@method_decorator([login_required, planner_required, finalisation_required], name='dispatch')
class RevertToPhase1(View):

    def get(self, request, *args, **kwargs):

        current_phase = self.request.user.phase
        # revert phase to phase 1
        if (current_phase == 3 ):
            User.objects.all().update(phase=1)
        return redirect('planners:currentphase')
