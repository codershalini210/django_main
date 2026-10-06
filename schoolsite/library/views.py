from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("use /books for books and /articles for articles")

def books(request):
    return render(request,'library/booklist.html')
    # return HttpResponse("this is books section of library")
def articles(request):
    return  HttpResponse("this is articles section of linrary")
