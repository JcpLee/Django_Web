#coding:utf-8  
from django.http import HttpResponse
from django.shortcuts import render
   
def index(request):  
    # return HttpResponse(u"Welcome,hello world!")
    return render(request,'login.html')
def zn(request):
    return render(request,'test.html')
def login(request):
    return render(request, 'index1.html')
def person(request):
    return render(request,'index.html')
def education(request):
    return render(request,'education.html')
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')

