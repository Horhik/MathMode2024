from flask import abort, redirect, url_for, render_template, Flask, request, session
from os import walk, makedirs
from database import make_users_folder, users_folder_exists, USER_FOLDER, create_user

def get_userlist():
    if users_folder_exists():
        users = next(walk('users'))[1]
        return users

    else:
        make_users_folder()
        return []
    

def user_exists(name):
    name = name.lower()
    users = get_userlist()
    return name in users

def login_user(name):
    name = name.lower()
    if user_exists(name):
        return redirect(url_for('profile', username=name))
    else:
        error = f"No such user \"{name}\", but you can register!"
        #register_user(name)
        print("TRYING  ", name, error)
        return redirect(url_for('registration', username=name,  preambola=error))

def register_user(name=""):
    name = name.lower()
    if user_exists(name) and name !='':
        return render_template('user_exists.html', name=name)
    else:
        create_user(name)
        return f'<p>User {name} created!<\p><p><a href="/profile/{name}">Go to messages!</a></p>'
        
    
