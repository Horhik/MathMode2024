from flask import abort, redirect, url_for, render_template, Flask, request, session
from users import user_exists
from database import get_chat_list, get_chat_data,append_new_message, get_chat_file, new_chat, generate_chat_header
from datetime import datetime
from bot import call_orwell
import json

def open_messenger(name):
    name = name.lower()
    if user_exists(name):
        chat_list = get_chat_list(name)
        return render_template('user_profile.html', name=name, chats=chat_list), 200
    
    else:
        return f'No such user: {name}'

def render_chat(username, chat):
    print("RENDERING WITH: ", username, chat)
    (header, messages) = get_chat_data(username, chat)
    messages = reversed(messages)
    return render_template("messenger.html", header=header, messages=messages, username=username), 200
    

def process_message(form, username, chat):
    text = form["message"]
    words = text.split(' ')
    message = json.dumps({"time": datetime.now().isoformat(), "sender": username, "text": text})
    append_new_message(message, get_chat_file(username, chat))

    if text[0] == '/':
        call_orwell(username, chat, command=words[0][1:], message=words[1:])
    


def create_new_chat(username, chat):
    if  chat not in get_chat_list(username) and user_exists(chat):
           header=generate_chat_header(username, chat)
           print(" header created! ", header)
           new_chat(header, username, chat)
           return redirect(f'/profile/{username}/messenger/{chat}')
    else:
        return '''
        Developer was too lazy to process this error. <br> So... <h1><b><i>There's an error</i></b></h1>
        <br> <small>
        probably no such user, or u're already chating with that person
        </small>
        <button onclick="history.back()">Go Back</button>
        '''
        


           
