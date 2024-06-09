# sticky_notes_app/forms.py

'''Form creation to register new users to the app.
Allows for the input of a user name, email address and password, 
with a secondary request to confirm the password'''

# Import necessary modules
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Define a custom User registration form that extends UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Add an email field to the form
    email = forms.EmailField()

    class Meta:
        # Specify the model to be used (User model)
        model = User
        # Define the fields to be displayed in the form
        fields = ['username', 'email', 'password1', 'password2']
