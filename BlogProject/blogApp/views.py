from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

posts = [
            {
                'title':'Blog Post 1',
                'author':'Red',
                'content':'This is my first blog post!',
                'date_posted':'12-12-2018'
            },
            {
                'title':'Blog Post 2',
                'author':'Red',
                'content':'This is my second blog post!',
                'date_posted':'03-01-2019'
            },
            {
                'title':'Blog Post 3',
                'author':'Red',
                'content':'This is my third blog post!',
                'date_posted':'12-01-2019'
            }
        ]

home_context = {
    'posts':posts,
    'title':'Home'
}

def home(request):
    return render(request, 'blogApp/home.html', context=home_context)


def about(request):
    return render(request, 'blogApp/about.html', {'title':'About'})