from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
# Create your views here.
def about(request):
    return HttpResponse("This is about us page")
def contact(request):
    return HttpResponse("This is Contact page")
def login(request):
    return render(request,'registration.html')

