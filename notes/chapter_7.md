Chapter 7: Large file structure (7a)
====================================

|-flasky
  |-app/
    |-templates/
    |-static/
    |-main/
      |-__init__.py
      |-errors.py
      |-forms.py
      |-views.py
    |-__init__.py
    |-email.py
    |-models.py
  |-migrations/
  |-tests/
    |-__init__.py
    |-test*.py
  |-venv/
  |-requirements.txt
  |-config.py
  |-manage.py


The project folder name is flasky.
There are four top level folders:

The flask application lives inside app.
Migrations scripts.
Tests folder.
Venv for virtual environment.


[requirements.txt] lists the package dependencies and you can regenerate a virtual environment.
[config.py] stores the configuration settings.
[manage.py] launches the application and other application tasks.

Config - apps need several config sets for dev, testing, and prod.  Use a base Config class and extend it.
init_app() takes an app instance as an argument

app - application package where all the code lives.  With a factory function (create_app(config_name) )
you can apply config settings and create multiple app instances.

Blueprints allow you to modularize your app

Run the unittests - python manage.py test


