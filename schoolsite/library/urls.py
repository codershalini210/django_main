from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/library/
    path("",views.home,name="home"),
    path("books",views.books,name="books"),
    path("articles",views.articles,name="articles")
]