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