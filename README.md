# Lab 6 – Introduction to Django and Flask Web Frameworks

## Overview
This lab demonstrates the development of simple web applications using two Python web frameworks: **Flask** and **Django**. The goal was to understand routing, templating, views, and how web applications are built and run locally.

---

# Flask Application

## Features Implemented
- Home route `/` displaying the message **"Welcome to Flask!"**
- Dynamic route `/hello/<name>` that displays **"Hello, <name>!"**
- Jinja2 template rendering
- Form where the user enters their name
- Form submission that displays a personalized greeting

## Project Structure
```
flask_app/
│
├── app.py
└── templates/
    ├── hello.html
    └── form.html
```
## How to Run the Flask App

1. Navigate to the Flask project folder

```
cd flask_app
```

2. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install Flask

```
pip install flask
```

4. Run the application

```
python3 app.py
```

5. Open in browser

```
http://127.0.0.1:5000
```
## output
<img width="956" height="372" alt="flask_output" src="https://github.com/user-attachments/assets/0678b2c0-991c-426d-9820-7ea5e1b9e1c1" />
 

# Django Application

## Features Implemented

- Homepage `/` displaying **"Hello from Django!"**
- Dynamic route `/greet/<name>/` for personalized greetings
- Django templating system for rendering HTML
- Message model with a text field
- Admin panel integration to manage messages
- View to display all stored messages

## Project Structure

```
django_app/
│
├── manage.py
├── greetings/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── templates/
    ├── home.html
    ├── greet.html
    └── messages.html
```
## How to Run the Django App

1. Navigate to the Django project folder

```
cd django_app
```

2. Install Django

```
pip install django
```

3. Apply migrations

```
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Create admin user

```
python3 manage.py createsuperuser
```

5. Run the server

```
python3 manage.py runserver
```

6. Open in browser

```
http://127.0.0.1:8000
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

## Output
<img width="961" height="606" alt="added message" src="https://github.com/user-attachments/assets/96326475-3c2f-4bc3-8875-cc0afa9d1929" />
<img width="956" height="299" alt="django_greeting" src="https://github.com/user-attachments/assets/37648ff0-e5df-46f6-bf53-07643591ed07" />
<img width="961" height="261" alt="greeting with name" src="https://github.com/user-attachments/assets/66ac3056-3bde-4fa6-972a-cf020e1ffe1a" />
<img width="960" height="523" alt="Django admin log in" src="https://github.com/user-attachments/assets/04fc9d34-f48c-4836-80b4-1eeb959cf0dd" />
<img width="956" height="382" alt="django hello" src="https://github.com/user-attachments/assets/d65852b0-c6d7-4649-abab-a5c93a78a417" />
<img width="960" height="319" alt="messages" src="https://github.com/user-attachments/assets/4b8f7373-04bc-478e-89ad-6c2b105b4f9b" />

