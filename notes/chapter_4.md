Chapter 4: Web forms with Flask-WTF (4a)
========================================

request.form provides access to form data submitted in POST requests.

HTML form code generation and validation for web forms is tedious.  This is handled by Flask-WTF, which is
a wrapper around the framework agnostic WTForms package.

To implement CSRF protection, Flask-WTF needs the application to configure an encryption key. Flask-WTF uses this key to
generate encrypted tokens that are used to verify the authenticity of requests with form data.

Store in an environment variable, not in the script
app.config['SECRET_KEY'] = 'secret'

Each class inherits from class Form, when using web forms.
Form fields are objects and validators are functions to check whether field is valid.

Use Bootstrap, if desired, to render forms easily
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}


Chapter 4: Redirects and user sessions (4b)
===========================================

Applications can remember things from one request to another by storing them in user sessions.

Redirections can route you to the endpoint provided.  url_for() takes the view function as an argument and
returns the URL endpoint.


Chapter 4: Message flashing (4c)
================================

Call flash() to collect messages to render between requests.  Use get_flashed_messages() in the template to render
the flashed message.


