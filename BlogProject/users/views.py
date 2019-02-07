from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        # If our request method is POST, then get the information from the request
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # If info is valid; save, get username, make message and redirect to blog-home
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else: # If request is GET, create empty form 
        form = UserRegisterForm()
    
    # Render if GET or if form.is_valid() == false
    return render(request, 'users/register.html', {'form':form})

