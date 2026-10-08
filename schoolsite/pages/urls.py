from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
     path("home", views.home, name="home"),
    path("about",views.about,name="about"),
    path("book",views.book,name="book"),
    path("department",views.departments,name="department")
]
