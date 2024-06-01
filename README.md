### Todo Application

## Description
The Todo Application is a task management web application that allows users to add, update, delete, and mark tasks as done. Tasks can be categorized as pending or done based on their completion status. 
Users can track the number of pending tasks, completed tasks, and manage their to-do list efficiently.

## Features
  - **Add Tasks:** Users can add new tasks to their to-do list.
  - **Update Tasks:** Edit task details such as description, due date, priority, etc.
  - **Delete Tasks:** Remove tasks from the list if they are no longer needed.
  - **Mark as Done:** Mark tasks as done once completed, moving them to the "Done" section.
  - **Task Categories:** Tasks are categorized as pending or done for easy management.
  - **Task Statistics:** View the number of pending tasks, completed tasks, and overall task status.
  
## Technologies Used
  - **Backend:** Python, Django
  - **Frontend:** HTML5, CSS3, JavaScript
  - **Database:** MySQL
  - **Template Engine:** Django Templates
  
## Files and Folders


- **TodoProject/:**
  - settings.py: Project settings including database configuration, static files, etc.
  - urls.py: Main URL configuration for routing requests to app-level URLs.
  
- **TodoApp/ (Django App):**
  - models.py: Defines models for tasks including fields like title, description, due date, status, etc.
  - views.py: Contains views for handling task operations (add, update, delete, mark as done).
  - urls.py: App-level URL configuration for routing requests to appropriate view functions.
  - static/: Folder containing CSS, JavaScript, and image assets for the frontend.
  - templates/: Folder containing HTML templates for rendering views and pages.

## Usage
  - Start the Django development server: python manage.py runserver
  - Open your web browser and visit http://localhost:8000/ to access the ExpenseTracker application.
  - Use the application to add, categorize, and manage your expenses.
