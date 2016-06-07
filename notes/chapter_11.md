Chapter 11: Blog posts (11a)
============================

A posts table is constructed as a model to support blog posts.  The posts are tied to some author, who
happens to be the User in our case.  We add a foreign key to the User class in order to reference it back
to the author.

The PostForm will let the user enter data.
Attempt to create a timeline for blog posts in the index view.


Chapter 11: Blog posts in profile pages (11b)
=============================================

The list of blog posts for a user is obtained from the User.posts relationship, which is a query object, 
so filters such as order_by() can be used on it as well.
The user.html template requires the <ul> HTML tree that renders a list of blog posts like the one in index.html. 
Having to maintain two identical copies of a piece of HTML is not ideal, so for cases like this, 
Jinja2’s include() directive is very useful.


Chapter 11: Generate fake users and posts (11c)
===============================================

As the blog posts grow, there will be too many.  The solution is to paginate and render in chunks.

A development dependency will not be used in production.  To test the blog, you can generate fake users/posts
with forgerypy.  Static methods are set in the User and Post models.  Enter a shell session to add to the db.


Chapter 11: Blog post pagination (11d)
======================================

Changes made to the home route to support pagination in the main folder
Pagination is defined in SQLAlchemy

A paginations footer is added with a macro and CSS


Chapter 11: Rich text blog posts with Flask-PageDown (11e)
==========================================================


• PageDown, a client-side Markdown-to-HTML converter implemented in Java‐ Script.
• Flask-PageDown, a PageDown wrapper for Flask that integrates PageDown with Flask-WTF forms.
• Markdown,aserver-sideMarkdown-to-HTMLconverterimplementedinPython.
• Bleach, an HTML sanitizer implemented in Python.

These packages will upgrade the blog posts from plain text to markdown.


Chapter 11: Rich text server side handling with Markdown and Bleach (11f)
=========================================================================

This is done to prevent CSRF


Chapter 11: Permanent links to posts (11g)
==========================================

The last feature related to blog posts is a post editor that allows users to edit their own posts. 
The blog post editor will live in a standalone page. 
At the top of the page, the current version of the post will be shown for reference, 
followed by a Markdown editor where the source Markdown can be modified.

