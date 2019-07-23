from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


usertypes = { 
    'professor': 1, 
    'eventplanners': 2, 
    'coursecoordinators': 3, 
    'timetableplanner': 4, 
    'student' : 5
}
 


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.user_type == usertypes['student']),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def professor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a professor,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.user_type == usertypes['professor']),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def coordinator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a coordinator,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.user_type == usertypes['coursecoordinators']),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def eventplanner_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is an event planner,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.user_type == usertypes['eventplanners']),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def planner_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a planner,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.user_type == usertypes['timetableplanner']),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def beforefirstdraft_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='403'):
    '''
    Decorator for views that checks that the current phase if phase 1
    redirects to the home page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.phase == 1),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def drafting_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='403'):
    '''
    Decorator for views that checks that the current phase is phase 2
    redirects to the home page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.phase == 2),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def finalisation_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='403'):
    '''
    Decorator for views that checks that the current phase is phase 3
    redirects to the home page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.phase == 3),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
