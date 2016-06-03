Chapter 3: Templates (3a)
=========================

The view function is in charge of handling the business logic.  This is the controller in the MVC pattern.
The business logic is concerned with getting information from forms, talking to the database, etc, but
we need to respond to the client with a page.  This is the presentation logic and we render templates that
are processed through the Jinja2 template engine.

Templates are found in the template folder and we can pass arguments to it.
Supports variables, control structures, and macros.

{{ variable|filter }} recognizes variables of any type
{% control %} control flow

{% if user %}
Hello, {{ user }} !
{% else %}
Hello stranger
{% endif %}

{% macro render_comment(comment) %}
	<li>{{ comment }}</li>
{% endmacro %}

<ul>
	{% for comment in comments %}
		{{ render_comment(comment) }}
	{% endfor %}
</ul>

block tags and a base.html class can be defined to allow for extension


Chapter 3: Templates with Flask-Bootstrap (3b)
==============================================

Bootstrap can be added without having to put the assets in the static folder.  Use the bootstrap extension.
This is in the base template using {% extends "bootstrap/base.html" %}

Many base template blocks are defined.  title, navbar, content in this example.

Many blocks already contain content.  Use super() to add more content so they aren't overriden.


Chapter 3: Custom error pages (3c)
==================================

Error handlers are present to make attractive custom errors when there is a problem.
@app.errorhandler(e) is invoked and an error status code can be returned.


