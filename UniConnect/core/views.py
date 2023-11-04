from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth import logout  # Import the logout function

from .forms import SignupForm, AccountSettingsForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] #show items 0-6
    categories = Category.objects.all() #show items 0-6

    return render(request, "core/index.html", {
        "categories" : categories,
        "items" : items,
    })

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
          form = SignupForm()

    return render(request, "core/signup.html", {
            "form" : form #pass form to front end
        })

def account(request):
    return render(request, 'core/logout.html')
def account_settings(request):
    # Implement your account settings view logic here
    return render(request, 'core/account_settings.html')

def logout_view(request):
    logout(request)
    # Redirect to a page or URL after logging out
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AccountSettingsForm  # Import your form
from django.contrib import messages

from django.db import IntegrityError  # Import IntegrityError

@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST)

        if form.is_valid():
            # Get the current user
            user = request.user
            # Retrieve the cleaned data from the form
            new_username = form.cleaned_data['new_username']
            new_email = form.cleaned_data['new_email']
            new_password = form.cleaned_data['new_password']

            # Handle username uniqueness check
            if new_username and new_username != user.username:
                try:
                    # Attempt to update the username
                    user.username = new_username
                    user.save()
                except IntegrityError:
                    messages.error(request, 'Username is already taken. Please choose a different username.')
                    return redirect('/account/settings/')

            if new_email:
                user.email = new_email
            if new_password:
                user.set_password(new_password)

            user.save()

            messages.success(request, 'Account settings updated successfully.')
        else:
            messages.error(request, 'Error updating account settings. Please correct the form.')

    else:
        # Get the current user's username and email to use as the initial value
        current_username = request.user.username
        current_email = request.user.email
        form = AccountSettingsForm(initial={'new_username': current_username, 'new_email': current_email})

    return render(request, 'core/account_settings.html', {'form': form})


