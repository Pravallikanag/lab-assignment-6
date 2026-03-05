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
 
