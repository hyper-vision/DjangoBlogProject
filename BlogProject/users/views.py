from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        # If our request method is POST, then get the information from the request
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # If info is valid; save, get username, make message and redirect to blog-home
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You may now log in!')
            return redirect('login')
    else: # If request is GET, create empty form 
        form = UserRegisterForm()
    
    # Render if GET or if form.is_valid() == false
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')