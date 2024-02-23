from flask import abort, redirect, url_for, render_template, Flask, request, session
from users import user_exists
from database import get_chat_list, get_chat_data,append_new_message
from datetime import datetime
import json

def open_messenger(name):
    name = name.lower()
    if user_exists(name):
        chat_list = get_chat_list(name)
        return render_template('user_profile.html', name=name, chats=chat_list), 200
    
    else:
        return f'No such user: {name}'

def render_chat(username, chat):
    (header, messages) = get_chat_data(username, chat)
    messages = reversed(messages)
    return render_template("messenger.html", header=header, messages=messages), 200
    

def process_message(form, username, chat):
    text = form["message"]
    message = json.dumps({"time": datetime.now().isoformat(), "sender": username, "text": text})
    append_new_message(message, username, chat)
    

