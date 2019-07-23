from django.contrib.auth.models import AbstractUser
from django.db import models

# To prevent hard-coding
usertypes = { 
    'professor': 1, 
    'eventplanners': 2, 
    'coursecoordinators': 3, 
    'timetableplanner': 4, 
    'student' : 5
}


USER_TYPE_CHOICES = (
    (1, 'professor'),
    (2, 'eventplanner'),
    (3, 'coursecoordinators'),
    (4, 'timetableplanner'),
    (5, 'student'),
)

PHASE_CHOICES = (
    (1, 'Phase 1'),
    (2, 'Phase 2'),
    (3, 'Phase 3'),
)


class User(AbstractUser):
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=5)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phase = models.PositiveSmallIntegerField(choices=PHASE_CHOICES, default=1)

    def get_user_type(self):
        if self.user_type == usertypes['professor']:
            return 'Professor'
        elif self.user_type == usertypes['coursecoordinators']:
            return 'Course Coordinator'
        elif self.user_type == usertypes['eventplanner']:
            return 'Event Planner'
        elif self.user_type == usertypes['timetableplanner']:
            return 'Timetable Planner'
        else:
            return 'Student'
            
    def get_phase(self):
        if self.phase == 1:
            return "Phase 1"
        elif self.phase == 2:
            return "Phase 2"
        elif self.phase == 3:
            return "Phase 3"
        else:
            return "None"

    def __str__(self):
        return self.username
