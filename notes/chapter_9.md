Chapter 9: User roles and permissions (9a)
==========================================

Not all users are created equal.  Some have more power than others. 
Here, users are assigned a discrete role, but the roles are defined in terms of permissions.

Permissions are represented as bit flags: follow, comment, write articles, moderate comments, administer

User roles:
anonymous: 	not logged in.  Read-only access.
user:		basic permission to write articles and comments. Follow others.
moderator:	permission to suppress comments.
admin:		full access, which includes permission to chnage the roles of other users.

Class method insert_roles() function, updates the roles in the database.
A new role or change in permission for a role can be added by invoking a shell session.

>>> Role.insert_roles()
>>> Role.query.all()
[<Role u'Administrator'>, <Role u'User'>, <Role u'Moderator'>]

Role assignment - when users register an account, the correct role should be assigned to them.
That is done in the User model constructor.

Role verification - a helper method can be added to the User model that checks whether a given
permission is present. The can() and is_administrator() functions do this.
