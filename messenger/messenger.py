from flask import abort, redirect, url_for, render_template, Flask, request, session
from users import user_exists
from database import get_chat_list

def open_messenger(name):
    name = name.lower()
    if user_exists(name):
        chat_list = get_chat_list(name)
        return render_template('user_profile.html', name=name, chats=chat_list), 200
    else:
        return f'No such user: {name}'
