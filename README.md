# StickyNotes App

Welcome to the StickyNotes App! This application allows you to create, view, update, and delete notes.

## Features

- **Create User**: Create an account to use the StickyNotes app.
- **Login**: Login to an exisiting user account.
- **Create Notes**: Easily create new notes with titles and content.
- **View Notes**: View all your existing notes with titles, content.and creation date.
- **Edit Notes**: Update the titles or content of existing notes.
- **Delete Notes**: Remove unwanted notes from your list.
- **Logout**: One button logout.

## Technologies Used

- **Django Framework**: Used for backend development, routing, and database management.
- **HTML/CSS**: For frontend layout and styling.
- **SQLite**: Database management system for storing notes data.

## Installation

1. Clone this repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```
    cd sticky_notes
    ```

3. Set up a virtual environment:
   
   ```
    python -m venv <virtual-environment-name>
   ```
   
5. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

6. Run the Django development server:

    ```
    python manage.py runserver
    ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

- **Homepage**:  Login or register using the respective buttons at the bottom of the page.
- **Add New Note**: Click on the "Create Note" link in the navigation menu and fill out the form.
- **Viewing Notes**: Access the 'Notes List' to see a list of all your existing notes.  Select a not to see more detail.
- **Edit a Note**: Click on the 'Edit Note' button inside the Note View.
- **Delete Note**: Click on the 'Delete Note' button inside the Note View.

