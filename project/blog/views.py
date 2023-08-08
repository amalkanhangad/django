from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

def home(request):
    posts = Post.objects.all()
    context={
        'name':'Akash',
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')


# Create your views here.
