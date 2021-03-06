Chapter 5: Database models with Flask-SQLAlchemy (5a)
=====================================================

Relational databases store data in tables.  These are the models of the application.
The collection of tables is called a schema.  The tables are related to each other through
relationships that consist of primary and foreign keys.

primary keys are unique identifiers.
foreign keys link tables together by pointing to a primary key.

(C)reate 	new tables and insert data into them
(R)ead      select the data you want from the tables and filter and order it in a set
(U)pdate    you can modify pre-existing data in the tables
(D)elete    get rid of records

SQLALCHEMY_DATABASE_URI  URL of the database
SQLALCHEMY_COMMIT_ON_TEARDOWN set to True for automatic commits after each request

Models are persistent entities of the db

Sqlite3 is a flat file database, not hosted on a server like a typical db, MySql, Oracle

Create Tables
=============
db.create_all()
db.drop_all()

Insert Rows
===========
Instantiate classes and assign them to variables
Changes to the database are added and committed through sessions

db.session.add_all([admin_role, mod_role])
db.session.commit()

To reverse changes:
db.session.rollback()

Query Rows
==========
Role.query.all()
User.query.filter_by(role=user_role).all()
Role.query.filter_by(name='User').first()


Chapter 5: Database use in the application (5b)
===============================================
Use SQL-Alchemy in the business logic instead of using sessions


Chapter 5: Shell context (5c)
=============================
To avoid having to constantly repeat these imports, the Flask-Script’s shell command can be configured to automatically import certain objects.

To add objects to the import list the shell command needs to be registered with a make_context callback function.


Chapter 5: Database migrations with Flask-Migrate (5d)
======================================================
A database migration framework is schema control.
Flask-Migrate is a wrapper around Alembic that can be accessed via Flask-Script.

Create a migration repo with a migrations folder, where scripts will be stored:
python hello.py db init

Create the script:
python hello.py db migrate -m "initial migration"

After reviewed:
python hello.py db upgrade			apply changes
python hello.py db downgrade		remove changes



