from django.shortcuts import render
from .models import Post 

home_context = {
    'posts': Post.objects.all(),
    'title':'Home'
} 

def home(request):
    return render(request, 'blogApp/home.html', context=home_context)


def about(request):
    return render(request, 'blogApp/about.html', {'title':'About'})