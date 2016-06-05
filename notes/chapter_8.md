Chapter 8: Password hashing with Werkzeug (8a)
==============================================

Authenticate with an app to make the user known.  When I use my email and password, I can authenticate with
Facebook or Gmail.  Then it knows its me, not someone else.

Flask-Login: Management of user sessions for logged-in users
Werkzeug: Password hashing and verification
itsdangerous: Cryptographically secure token generation and verification

Passwords are cryptographically hashed when stored in the database
Werkzeug's security module implements hashing


Chapter 8: Authentication blueprint (8b)
========================================

Organize app by functionality.  All authorization functions go into /auth


Chapter 8: Login and logout with Flask-Login (8c)
=================================================
Flask-Login remembers the user has been logged-in between requests.

UserMixin is a base class in Flask-Login to inherit from.  Extend the User model with UserMixin for default settings.
login_manager = LoginManager()
login_manager.session_protection = 'strong'		Keeps track of browser agent and IP address
login_manager.login_view = 'auth.login'			Endpoint for the login page

Protect routes for authenticated users only
Add this decorator 
@login_required

Chapter 8: User registration (8d)
=================================
When new users want to become members of the application, they must register with it so that they are known and can log in. A link in the login page will send them to a registration page, where they can enter their email address, username, and password.




