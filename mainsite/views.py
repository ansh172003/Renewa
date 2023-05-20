from django.shortcuts import render
from .models import BlogModel
# Create your views here.

def home(request):
    blogs = BlogModel.objects.all()
    data={
        'blogs':blogs,

    }
    return render(request,'mainsite/landing.html',data)

def blogs(request):
    blogs = BlogModel.objects.all()
    data={
        'blogs':blogs,

    }
    return render(request,'mainsite/blogpost.html',data)
    

def food(request):
    pass

def recipe(request):
    pass

def grocery(request):
    pass

def donate(request):
    return render(request, 'mainsite/donate.html')