# Review Flask Project 📝
Built with Python, Flask, SQLAlchemy, Flask-Bcrypt, and Flask-Login.

A web application where users can register, log in, and create, edit, and delete posts, with secure authentication and profile picture uploads.

---

---

# Part 1 — Setup

---

## Step 1 — Clone the repository

In bash terminal enter:
```
git clone https://github.com/misael-mercado/Review_Flask_Project.git
```
Then navigate into the project folder:
```
cd Review_Flask_Project
```

---

## Step 2 — Create a virtual environment

In bash terminal enter:
```
python3 -m venv venv
```
Then activate it:

On Mac/Linux:
```
source venv/bin/activate
```
On Windows:
```
venv\Scripts\activate
```

---

## Step 3 — Install dependencies

In bash terminal enter:
```
pip install flask flask-sqlalchemy flask-bcrypt flask-login flask-wtf email-validator pillow
```

---

## Step 4 — Add your secret key

Open `review_flask/__init__.py` and find this line:
```
app.config['SECRET_KEY'] = 'PUT YOUR OWN SECRET KEY HERE!'
```
To generate your own secret key, in bash terminal enter:
```
python3 -c "import secrets; print(secrets.token_hex(16))"
```
The terminal will print something like:
```
a3f1c92de845b67f2190acd33e78b421
```
Copy that value and replace `PUT YOUR OWN SECRET KEY HERE!` with it.

---

## Step 5 — Set up the database

In bash terminal enter:
```
python3
```
You will enter a Python shell. Then enter these one at a time:
```
from review_flask import db
```
```
db.create_all()
```
```
exit()
```
You should see a `mydb.sqlite` file appear inside the `instance/` folder. That is your database.

---

## Step 6 — Run the app

In bash terminal enter:
```
python3 run.py
```
Then open your browser and go to:
```
http://localhost:5000
```

---

---

# Part 2 — How It Works

---

## Registering a user

When someone fills out the register form, this is what happens:

```
1. Form validates username and email are not already taken
         ↓
2. Password is hashed with bcrypt before saving
         ↓
3. New User is added to the database
         ↓
4. Flash message confirms account was created
         ↓
5. User is redirected to the login page
```

---

## Logging in

When someone fills out the login form, this is what happens:

```
1. App looks up the user by email in the database
         ↓
2. bcrypt checks the submitted password against the stored hash
         ↓
3. If correct, Flask-Login logs the user in and sets a session
         ↓
4. If Remember Me is checked, a cookie keeps them logged in
         ↓
5. User is redirected to home or the page they were trying to visit
```

---

## Creating a post

When a logged in user submits the create post form, this is what happens:

```
1. Form validates title and content are not empty
         ↓
2. New Post is created and linked to the current user as author
         ↓
3. Post is saved to the database
         ↓
4. Flash message confirms the post was created
         ↓
5. User is redirected to the home page where the post appears
```

---

## Updating a post

When a logged in user updates one of their posts, this is what happens:

```
1. App checks that the current user is the author of the post
         ↓
2. If not the author, a 404 error is returned
         ↓
3. If the author, the existing title and content are loaded into the form
         ↓
4. On submit, the post is updated in the database
         ↓
5. Flash message confirms the update and user is redirected to the post
```

---

## Deleting a post

When a logged in user deletes one of their posts, this is what happens:

```
1. App checks that the current user is the author of the post
         ↓
2. If not the author, a 404 error is returned
         ↓
3. Post is deleted from the database
         ↓
4. Flash message confirms deletion
         ↓
5. User is redirected to the home page
```

---

## Updating your account

When a logged in user updates their profile, this is what happens:

```
1. Form validates the new username and email are not taken
         ↓
2. If a new picture was uploaded, it is resized to 125x125
         ↓
3. Picture is saved to static/profile_pics/ with a random hex filename
         ↓
4. Username, email, and image_file are updated in the database
         ↓
5. Flash message confirms the update was saved
```

---

## Project file structure

```
Review_Flask_Project/
├── review_flask/
│   ├── static/
│   │   ├── profile_pics/     → uploaded profile pictures
│   │   └── main.css          → stylesheet
│   ├── templates/            → HTML pages
│   │   ├── layout.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── account.html
│   │   ├── create_post.html  → used for both new and update post
│   │   └── post.html         → single post view with edit/delete buttons
│   ├── __init__.py           → app setup, database, bcrypt, login manager
│   ├── forms.py              → register, login, account update, and post forms
│   ├── models.py             → User and Post database models
│   └── routes.py             → all app routes and logic
├── run.py                    → entry point to run the app
└── README.md
```

---

---

# Part 3 — Example Demo

---

## Example: Registering an account

Open your browser and go to:
```
http://localhost:5000/register
```
Fill in your details and click **Sign Up**. The browser will show:
```
Your account has now been created! You can now log in.
```
You will be redirected to the login page.

If the username is already taken, you will see:
```
That username is taken. Please choose a new one.
```

If the email is already taken, you will see:
```
That email is taken. Please choose a new one.
```

---

## Example: Logging in

Open your browser and go to:
```
http://localhost:5000/login
```
Enter your email and password and click **Login**. You will be redirected to the home page.

If your credentials are wrong, you will see:
```
Login Unsuccessful. Please check email and password
```

---

## Example: Creating a post

Once logged in, click **New Post** in the navigation bar. You will be taken to:
```
http://localhost:5000/post/new
```
Fill in a title and content and click **Post**. You will see:
```
Your post has been created!
```
You will be redirected to the home page where your post appears.

---

## Example: Updating a post

Click on a post you authored. You will be taken to:
```
http://localhost:5000/post/1
```
Click **Update**. The form will load with your existing title and content. Make your changes and click **Post**. You will see:
```
Your post has been updated!
```
If you try to update someone else's post, you will get a 404 error.

---

## Example: Deleting a post

Click on a post you authored and click **Delete**. A confirmation modal will appear. Confirm the delete and you will see:
```
Your post has been deleted!
```
You will be redirected to the home page. If you try to delete someone else's post, you will get a 404 error.

---

## Example: Updating your profile

Once logged in, click **Account** in the navigation bar. You will be taken to:
```
http://localhost:5000/account
```
Update your username or email and click **Update**. You will see:
```
Your account has been updated!
```
To upload a profile picture, click **Choose File** and select a jpg, jpeg, or png. It will be automatically resized to 125x125 pixels before saving.

---

## Example: Logging out

Click **Logout** in the navigation bar. You will be redirected to the home page and your session will be cleared.

If you try to visit a protected page like `/account` or `/post/new` while logged out, you will be redirected to:
```
http://localhost:5000/login
```