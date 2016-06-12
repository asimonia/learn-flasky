Chapter 13: Blog post comments (13a)
====================================

Comments apply to specific blog posts, so a one-to-many relationship from the posts table is defined.
The relationship can be used to obtain the list of comments associated with a particular blog post.

The comments is one-to-many with the users table.  This relationship gives access to all the comments made by a user, and indirectly how many comments a user has written.

The comments table is added.

A simple webform is added to submit the comments.
The blog post comments support is added as a view to the main blueprint.