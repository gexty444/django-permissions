# django-permissions
A simple project to show the implementation of permissions in Django to restrict views for different users. There are two types of permissions in this project -- **user types** and **phase**. Each user type can only access the pages available to them and will be redirected to the login page when they try to access other pages. 

The permissions for the different phases are done (via decorators and in the user model) but pages only accessible during a certain phase are not created in this project. Such views can be easily done up with the use of the correct phase decorator in `decorator.py`. You can  check out [this repository](https://github.com/gexty444/50.003_ESC) where the phases permissions were implemented. Try logging in as a timetable planner and change up the phases!

Sorry for the poorly named user types, they were taken from a previous project! :)

