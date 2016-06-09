Chapter 12: Database representaton of followers (12a)
=====================================================


Users are able to follow others and limit to what they see from their followers.

An association table will decompose the many-to-many relationship between two tables to many-to-one.

Followers are a many-to-many relationship.  The user can follow others and can be followed by other users.
An association table called 'follows' takes care of this.

