Chapter 8: Password hashing with Werkzeug (8a)
==============================================

Authenticate with an app to make the user known.  When I use my email and password, I can authenticate with
Facebook or Gmail.  Then it knows its me, not someone else.

Flask-Login: Management of user sessions for logged-in users
Werkzeug: Password hashing and verification
itsdangerous: Cryptographically secure token generation and verification

Passwords are cryptographically hashed when stored in the database
Werkzeug's security module implements hashing

