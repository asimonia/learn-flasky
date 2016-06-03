Chapter 2: A complete application (2a)
======================================

Applications require three layers.

1) To create the flask app, import the Flask class and instantiate the Flask object.
Pass the __name__ arg in to call the constructor so Flask knows where to find templates and static files.

2) Define the routes associated with the app and assign them URLs.  The decorator wraps the view function.
The view function receives the request object, manipulates it and returns a response.

3) Run the app by invoking the run method.  Set debug=True allows debugging the stack trace.

The app will be running on local host in production mode.


Chapter 2: Dynamic routes (2b)
==============================

Flask routes can be dynamic.  When entering the URL in the browser, you can add variables
'/user/<name>'
'/user/<name>/<int:age>'

Pass the variable to the view function.  You can return variables in the response.


