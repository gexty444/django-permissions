from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from ..decorators import eventplanner_required
from ..forms import EventPlannerSignUpForm
from ..models import User

usertypes = { 
    'professor': 1, 
    'eventplanners': 2, 
    'coursecoordinators': 3, 
    'timetableplanner': 4, 
    'student' : 5
}


class EventPlannerSignUpView(CreateView):
    model = User
    form_class = EventPlannerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'eventplanners'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        userdetail = form.save(commit=False)
        try:
            userdetail.phase = User.objects.filter(user_type=usertypes['professor'])[0].phase
        except:
            userdetail.phase = 1
        userdetail = form.save()
        login(self.request, userdetail)
        return redirect('eventplanner:eventplanner_main')


@method_decorator([login_required, eventplanner_required], name='dispatch')
class EventPlannerMainView(TemplateView):
    template_name = 'users/eventplanner/eventplanner_main.html'

