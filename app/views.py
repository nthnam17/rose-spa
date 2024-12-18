from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context={}
    return render(request,'app/home.html',context)
def service(request):
    context={}
    return render(request,'app/service.html',context)
def register(request):
    context={}
    return render(request,'app/register.html',context)