from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Create an instance of the new field we want to add

    class Meta: # Allows us to redefine variables form the parent class (UserCreationForm), from within the child class
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # Fields and the order in which they should appear