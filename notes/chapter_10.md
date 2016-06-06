Chapter 10: User profiles (10a)
===============================

Social websites have a user profile page.  Additional information can be recorded
by using new fields in the User model.

Add a User profile template and view.


Chapter 10: Profiles editor (10b)
=================================

Two different profile editing forms: one for admin and one for user.

EditProfileForm(Form)
EditProfileAdminForm(Form)


Chapter 10: User avatars (10c)
==============================

Gravatar generates avatars with email hashes.
http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6


Chapter 10: Caching of user avatar hashes (10d)
===============================================

Store the avatar hashes so they won't have to be generated on the fly each time page is loaded.