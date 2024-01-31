# Blog Application
Develop a simple blog application using Django that allows users to read and create blog posts.

Basic Features of The App:-
1. User Authentication:
Users can sign up with a unique username and password.
Registered users can log in securely and log out when they're done.
Authentication ensures that only authorized users can create and manage their own blog posts.

2. Blog Post Management (CRUD Operations):
Users can create new blog posts by providing a title and body content.
They can view their existing posts, edit them, update content, or delete posts they no longer want.
CRUD operations ensure the basic functionalities required for managing blog content.

3. Viewing Blog Posts:
The home page of the application displays all blog posts in reverse chronological order, allowing users to see the latest posts first.
Each post title is clickable, directing users to a page displaying the full details of the selected post, including its title and body content.

4. Administration Panel:
The application utilizes Django's built-in admin panel for administrative tasks.
Admin users have elevated privileges allowing them to perform CRUD operations on all blog posts.
They can create new posts, edit existing ones, and delete posts as necessary, offering full control over the blog content.

5.Technology Stack:
The project is built using Django, a high-level Python web framework, for backend development.
Django provides built-in features for user authentication, database management, and admin panel creation, facilitating rapid development.
For the frontend, HTML, CSS, and possibly JavaScript are used to design the user interface and interact with the backend functionalities.



Quick Start:

To get this project up and running locally on your computer follow the following steps.

Set up a python virtual environment
Run the following commands

1. cd ~/Destop/BlogApplication
2. python -m venv env
3. env\Scripts\activate
4. pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver
   
Open a browser and go to http://localhost:8000/
