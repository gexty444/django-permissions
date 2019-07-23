"""differentusers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from main.views import main, students, professors, coordinators, planners, eventplanners

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # urls for registration, login and logout
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', main.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/professor/', professors.ProfessorSignUpView.as_view(), name='professor_signup'),
    path('accounts/signup/coordinator/', coordinators.CoordinatorSignUpView.as_view(), name='coordinator_signup'),
    path('accounts/signup/planner/', planners.PlannerSignUpView.as_view(), name='planner_signup'),
    path('accounts/signup/event/', eventplanners.EventPlannerSignUpView.as_view(), name='eventplanner_signup'),
    # include other urls from other apps
]