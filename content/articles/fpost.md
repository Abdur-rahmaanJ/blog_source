Title: My First Blog Post
Author: Abdur-Rahmaan Janhangeer
Date: 2019-01-01 9:00
Category: blogging
Tags: python, markdown, pelican
Slug: my-first-blog-post

Blog post content goes here

Code blocks are preceeded by an indent, three : symbols and the name of the language.  
All of the following code will be highlighted while the text is indented.

    :::python3
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)