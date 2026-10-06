from django.urls import path
from . import views
urlpatterns=[
    path("welcome",views.welcome,name="welcome"),
    path("courses",views.courses,name="courses"),
    path("",views.home,name="home"),
]