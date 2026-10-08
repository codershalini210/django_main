from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Book
def home(request):
    # return HttpResponse("hello world hwo are aj")
    return render(request,"pages/home.html")
def about(request):
    return render(request,"pages/about.html")
def book(request):
    books = Book.objects.all()
    return render(request,"pages/booklist.html",{"books":books})