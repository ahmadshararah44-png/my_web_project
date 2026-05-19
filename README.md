Project Title
Web-Based Task and Data Management System using Django


Research Problem
How to manage dynamic web views, user paths, and project structure effectively within the Django environment, while handling data safely.

Motivation
To build a complete backend structure using Django's framework, learn how URLs map to views, and manage database setup correctly for web applications.


Control Flow
1 Browser Request: The client requests a specific page from the browser.
2 URL Routing: Django's URL router maps the request to the correct view file.
3 View Logic: The view handles the backend logic and database operations.
4 Template Render: The dynamic HTML template renders the final page back to the user.


Implementation Strategy
 Modular Architecture: Separated the code into models for data, views for logic, and templates for design.
 Routing Configuration: Maintained clean routing paths to keep the project organized and easy to expand.

 
Setup and Usage Documentation
1 Clone the repository to your desktop.
2 Create and activate a python virtual environment.
3 Run the command "python manage.py migrate" to configure the project data.
4 Run "python manage.py runserver" to start the server locally.
