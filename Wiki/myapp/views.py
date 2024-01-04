from django.shortcuts import render
from django.http import HttpResponse #imports httpResponse class from django.http module

# Create your views here.

#define an index function that takes a request object as its parameter
#returns a HttpResponse object with the string "Hello, Wiki!" as its content
def index(request):
    return render(request, "./index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "./greet.html", {
        "name": name.capitalize()
    })