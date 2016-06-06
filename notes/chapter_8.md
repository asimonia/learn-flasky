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


Chapter 8: Account confirmation (8e)
====================================
To ensure the information is valid, the user needs to be able to be contacted through email.
itsdangerous generates confirmation tokens.  The user can click on the email with the confirmation
token to go from unconfirmed to confirmed.

http:// www.example.com/auth/confirm/<id>
To encrypt the id, so not any user can access, the id is replaced with the confirmation token.
TimedJSONWebSignatureSerializer generates JSON Web Signatures (JWS) with a time expiration.
SECRET_KEY is the encryption key argument.
dumps() generate a cryptographic signature and then serializes the data plus the 
signature as a convenient token string.
loads() decodes the token.


Sending confirmation emails


The before_app_request handler will intercept a request when three conditions are true:
1. A user is logged in (current_user.is_authenticated() must return True).
2. The account for the user is not confirmed.
3. The requested endpoint (accessible as request.endpoint) is outside of the au‐ thentication blueprint. Access to the authentication routes needs to be granted, as those are the routes that will enable the user to confirm the account or perform other account management functions.
If the three conditions are met, then a redirect is issued to a new /auth/unconfirmed route that shows a page with information about account confirmation.

Chapter 8: Password updates (8f)
================================
Create a new form security feature.

Chapter 8: Password resets (8g)
===============================
To avoid locking users out of the application when they forget their passwords, a password reset option can be offered. To implement password resets in a secure way, it is necessary to use tokens similar to those used to confirm accounts. When a user requests a password reset, an email with a reset token is sent to the registered email address. The user then clicks the link in the email and, after the token is verified, a form is presented where a new password can be entered.

Chapter 8: Email address changes (8h)
=====================================

