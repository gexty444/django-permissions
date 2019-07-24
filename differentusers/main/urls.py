from django.urls import include, path

from .views import main, students, professors, coordinators, planners, eventplanners


urlpatterns = [
    path('', main.home, name='home'),
    path('403', main.ForbiddenView.as_view(), name='403'),

    path('students/', include(([
        path('', students.StudentMainView.as_view(), name='student_main'),
    ], 'main'), namespace='students')),

    path('professors/', include(([
        path('', professors.ProfessorMainView.as_view(), name='professor_main'),
    ], 'main'), namespace='professors')),

    path('coordinators/', include(([
        path('', coordinators.CoordinatorMainView.as_view(), name='coordinator_main'),
    ], 'main'), namespace='coordinators')),

    path('planners/', include(([
        path('', planners.PlannerMainView.as_view(), name='planner_main'),
        path('phase', planners.CurrentPhase.as_view(), name='currentphase'),
        path('nextphase', planners.NextPhase.as_view(), name="nextphase"),
        path('prevphase', planners.PreviousPhase.as_view(), name="prevphase"),
    ], 'main'), namespace='planners')),

    path('event/', include(([
        path('', eventplanners.EventPlannerMainView.as_view(), name='eventplanner_main'),
    ], 'main'), namespace='eventplanners')),
]