from flask import abort, redirect, url_for, render_template, Flask, request, session
from messenger import open_messenger, render_chat, process_message
from users import login_user, register_user, get_userlist 
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/users')
def users():
    return  get_userlist()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/profile/<username>')
def profile(username):
    return open_messenger(name=username)

@app.route('/<username>/messenger/<chat>', methods=['GET', 'POST'])
def chat(username, chat):
    #data = get_chat_data(username, chat)
    if request.method == 'POST':
        process_message(request.form, username, chat)
        return render_chat(username, chat )
    else:
        return render_chat(username, chat )
#Path("users", username, "messages", chat).read_text()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = (request.form['username'])
        return login_user(name)
    return '''
        <h1> LOGIN </h1>
        <form method="post">
            <p>login: <input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/register',  methods=['GET', 'POST'])
@app.route('/register/<username>:message=<preambola>',  methods=['GET', 'POST'])
def registration(username='', preambola=None):
    print("REGISTRATING", username)
    if request.method == 'POST':
        name = (request.form['username'])
        return register_user(name=name)
    return render_template('registration.html', default_name=username, preambola=preambola)

