from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Book,Department
def home(request):
    # return HttpResponse("hello world hwo are aj")
    return render(request,"pages/home.html")
def about(request):
    return render(request,"pages/about.html")
def book(request):
    books = Book.objects.all()
    return render(request,"pages/booklist.html",{"books":books})
def departments(request):
    departments = Department.objects.all()
    return render(request,"pages/department_list.html",{"departments":departments})