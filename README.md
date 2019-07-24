# django-permissions
A simple project to demonstrate the implementation of permissions in Django to restrict views for different users. There are two types of permissions in this project -- **user types** and **phase**. 

### User Types
There are 5 user types in this project -- professors, event planners, course coordinators, timetable planners and students. (See `models.py`) Each user type can only access the pages available to them and will be **redirected** to the login page when they try to access other pages.

### Phase
The permissions for the different phases are done (via decorators and in the user model) but pages only accessible during a certain phase are not created in this project. Such views can be easily done up with the use of the correct phase decorator in `decorators.py`. You can  check out [this repository](https://github.com/gexty444/50.003_ESC) where the phases permissions were implemented. Try logging in as a timetable planner and change up the phases!

The view for reverting back to phase 1 is restricted to when we are in phase 3. (See `RevertToPhase1` in `main\views\planners.py`) However, the url for this view is not added, so at the moment you can't visualise the redirect when we try to access this view in phase 1 or phase 2. (You can do this as an exercise!) 

_Sorry for the poorly named user types, they were taken from a previous project! :)_

