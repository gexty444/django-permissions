from django.shortcuts import redirect, render
from django.views.generic import TemplateView

usertypes = { 
    'professor': 1, 
    'eventplanners': 2, 
    'coursecoordinators': 3, 
    'timetableplanner': 4, 
    'student' : 5
}

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.user_type == usertypes['professor']:
            return redirect('professors:professor_main')
        elif request.user.user_type == usertypes['coursecoordinators']:
        	return redirect('coordinators:coordinator_main')
        elif request.user.user_type == usertypes['timetableplanner']:
            return redirect('planners:planner_main')
        elif request.user.user_type == usertypes['eventplanners']:
            return redirect('eventplanners:eventplanner_main')
        else:
            return redirect('students:student_main')
    return render(request, 'users/home.html')

class ForbiddenView(TemplateView):
    template_name = '403.html'



