from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='login')
def homepage(request):
    # This view function renders the homepage.html template for authenticated users only.
    # If a non-authenticated user tries to access this URL, they will be redirected to the login page.
    context = {"title":"Homepage"}
    return render(request, 'homepage.html', context)

def signup(request):
    # This view function handles user sign-up functionality.

    if request.method == 'POST':
        # If the request method is POST, it means the user submitted the signup form.
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # If the form data is valid, save the user to the database and redirect to the homepage.
            form.save()
            return redirect('/')
        else:
            # If the form data is invalid, display an error message to the user.
            messages.error(request, f'Oops, something went wrong, try to signup again!')

    else:
        # If the request method is not POST, it means the user is accessing the signup page for the first time.
        # In this case, create an instance of the UserCreationForm to render the signup form.
        form = UserCreationForm()

    # Prepare the context dictionary with the form to be rendered in the signup.html template.
    context = {'form': form, "title":"Signup"}
    return render(request, 'signup.html', context)
