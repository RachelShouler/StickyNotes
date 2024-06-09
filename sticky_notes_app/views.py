# Import necessary modules
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# login_required ensures only logged-in users can access specified views
from django.contrib.auth.decorators import login_required
from .models import StickyNotes
from .forms import UserRegisterForm


def index(request):
    """
    View for displaying the index page.
    Retrieves all StickyNotes objects from the database and renders them
    on the index.html template.
    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML response containing the index page with a
        list of StickyNotes.
    """
    posts = StickyNotes.objects.all()
    return render(request, 'sticky_notes_app/index.html', {'posts': posts})


def register(request):    # For new users to register
    """
    View for user registration.
    Handles user registration form submission. If the form is valid, a
    new user account is created.
    Redirects to the login page upon successful registration.
    Args:
        request: The HTTP request object.
    Returns:
        Rendered HTML response containing the registration form or a
        redirect to the login page.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)    # From forms.py
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'sticky_notes_app/register.html', {'form': form})


def login_view(request):
    """
    View function for handling user login.
    Args:
        request: The HTTP request object.
    Returns:
        If the request method is POST:
            - Validates the login form.
            - If valid, authenticates the user and logs them in.
            - If invalid, displays error messages for incorrect details.
        Otherwise:
            - Renders the login.html template with an empty login form.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)    # Correct login
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index')
            else:    # Error message for incorrect details
                messages.error(request, 'Invalid username or password.')
        else:    # Error message for incorrect details
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'sticky_notes_app/login.html', {'form': form})


def logout_view(request):
    """
    View for logging out the user.
    :param request: HTTP request object
    :return: Redirects to the 'index' page after successful logout
    """
    logout(request)    # Successful logout message
    messages.info(request, 'You have successfully logged out.')
    return redirect('index')


def protected_view(request):
    """
    View for accessing a protected page.
    :param request: HTTP request object
    :return: Redirects to the 'login' page if the user is not
    authenticated, otherwise renders 'protected.html'
    """
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'sticky_notes_app/protected.html')


@login_required(login_url="login")    # Protected page - logged in only
def notes_index(request):
    """
    View for displaying a list of sticky notes.
    :param request: HTTP request object
    :return: Renders 'notes_index.html' with a list of sticky notes
    """  
    posts = StickyNotes.objects.all()
    return render(request, 'sticky_notes_app/notes_index.html', {'posts': posts})


@login_required(login_url="login")    # Protected page - logged in only
def add_note(request):
    """
    View for adding a new sticky note.
    :param request: HTTP request object
    :return: Redirects to 'notes_index' page after creating a new note
    or renders 'add_note.html' for form submission
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Below is the ORM to create a new note record in the table
        StickyNotes.objects.create(title=title, content=content)
        # When done, return to the index.html page
        return redirect('notes_index')
    return render(request, 'sticky_notes_app/add_note.html')


@login_required(login_url="login")    # Protected page - logged in only
def view_note(request, post_id):
    """
    View function for displaying a single sticky note.
    Args:
        request: The HTTP request object.
        post_id: The ID of the sticky note to be displayed.

    Returns:
        Renders the view_note.html template with the data of the
        specified sticky note.
    """
    post = get_object_or_404(StickyNotes, id=post_id)
    return render(request, 'sticky_notes_app/view_note.html', {'post': post})


@login_required(login_url="login")    # Protected page - logged in only
def edit_note(request, post_id):
    """
    View function for editing a sticky note.
    Args:
        request: The HTTP request object.
        post_id: The ID of the sticky note to be edited.
    Returns:
        If the request method is POST, updates the sticky note with the
        new title and content,
        and redirects to the view_note page for the updated note.
        Otherwise, renders the edit_note.html template with the sticky
        note data.
    """
    post = get_object_or_404(StickyNotes, id=post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        # Redirect to the view_post page
        return redirect('view_note', post_id=post.id)
    return render(request, 'sticky_notes_app/edit_note.html', {'post': post})


@login_required(login_url="login")    # Protected page - logged in only
def delete_note(request, post_id):
    """
    View for deleting a note.
    Handles note deletion. Deletes the specified StickyNotes object
    from the database.
    Args:
        request: The HTTP request object.
        post_id: The ID of the note to be deleted.
    Returns:
        Rendered HTML response indicating the deletion of the note.
    """
    post = get_object_or_404(StickyNotes, id=post_id)
    post.delete()
    return render(request, 'sticky_notes_app/deleted_note.html', {'post': post})
