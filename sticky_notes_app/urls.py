"""
URL configuration for sticky_notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import necessary modules
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Maps the root URL to the `index` view - login page
    path('', views.index, name='index'),
    # Handles new user registration
    path('register/', views.register, name='register'),
    # Handles user login
    path('login/', views.login_view, name='login'),
    # Handles user logout
    path('logout/', views.logout_view, name='logout'),
    # Protected view for users who are not logged in
    path('protected/', views.protected_view, name='protected'),
    # Notes index showing all notes created by the user
    path('notesIndex', views.notes_index, name='notes_index'),
    # Adds a new note
    path('add/', views.add_note, name='add_note'),
    # Allows user to view a specific note
    path('post/<int:post_id>/', views.view_note, name='view_note'),
    # Allows user to edit a specific note
    path('edit/<int:post_id>', views.edit_note, name='edit_note'),
    # Allows user to delete a note
    path('deletePost/<int:post_id>', views.delete_note, name='delete_note')
]
