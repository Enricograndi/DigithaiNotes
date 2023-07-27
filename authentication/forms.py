from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    # Custom form fields for first name, last name, and email
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        # Get the entered username from cleaned_data dictionary
        username = self.cleaned_data.get('username')
        # Get the User model from the Meta class
        model = self.Meta.model
        # Check if any user with the same username exists in the database (case-insensitive)
        user = model.objects.filter(username__iexact=username)
        
        if user.exists():
            # Raise a validation error if the username already exists
            raise forms.ValidationError("A user with that name already exists")
        
        return self.cleaned_data.get('username')

    def clean_email(self):
        # Get the entered email from cleaned_data dictionary
        email = self.cleaned_data.get('email')
        # Get the User model from the Meta class
        model = self.Meta.model
        # Check if any user with the same email exists in the database (case-insensitive)
        user = model.objects.filter(email__iexact=email)
        
        if user.exists():
            # Raise a validation error if the email already exists
            raise forms.ValidationError("A user with that email already exists")
        
        return self.cleaned_data.get('email')

    def clean_password(self):
        # Get the entered password from cleaned_data dictionary
        password = self.cleaned_data.get('password')
        # Get the entered confirm password from the form data
        confirm_password = self.data.get('confirm_password')
        
        if password != confirm_password:
            # Raise a validation error if passwords do not match
            raise forms.ValidationError("Passwords do not match")

        return self.cleaned_data.get('password')
