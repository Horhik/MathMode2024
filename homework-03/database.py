from os import walk, makedirs
from pathlib import Path
import json

USER_FOLDER = 'users'
POOL_FILE   = 'data/pool'
DATA_FOLDER = 'data'
USER_MESSAGES = "messages"

def folder_exists(p):
    path = Path(p)
    return path.exists() and path.is_dir()

def users_folder_exists():
    return folder_exists(USER_FOLDER)

def make_users_folder():
    Path(USER_FOLDER).mkdir()

def setup_user(name):
    #Create a global pool if not exsits
    Path(DATA_FOLDER).mkdir(parents=True, exist_ok=True)
    pool = Path(POOL_FILE).absolute()
    pool.touch()
    header = json.dumps({"Pool with ": name , "participants": [name]})
    append_new_message(header, pool)

    #Create messages folder
    user_messages = Path(USER_FOLDER, name, 'messages')
    user_messages.mkdir(exist_ok=True, parents=True)

    #Symlink pool to messages
    user_pool = Path(user_messages, "pool").absolute()
    user_pool.symlink_to(pool)
    user_pool.resolve()


def create_user(name):
    name = name.lower()
    makedirs(f'{USER_FOLDER}/{name}')
    setup_user(name)

def get_chat_list(name):
    return list(map(lambda x: x.name, Path(USER_FOLDER, name, USER_MESSAGES).iterdir()))

def get_chat_file(name,chat):
    print("Getting chat file: ", name, chat)
    return Path(USER_FOLDER, name, USER_MESSAGES, chat)

def append_new_message(message, chat_file):
    with chat_file.open("a") as f:
        f.write(message + '\n')
    
def generate_chat_header(name, chat):
    header = {"name": name + " - " + chat, "participants": [name, chat]}
    return json.dumps(header)


def get_chat_data(name, chat): # -> (chat_header, messages_array)
    chat_file = get_chat_file(name, chat).open()
    jsons = list(map(lambda x: json.loads(x), chat_file.readlines()))
    chat_header  = jsons[0]
    messages = jsons[1:]
    chat_file.close()
    return (chat_header, messages)

    


def new_chat(header, name, chat_name):
    chat_file = get_chat_file(name, chat_name)
    chat_file.touch()

    # Linking created file to another user
    connected_user_path = Path(USER_FOLDER, chat_name, "messages", name ).absolute()
    connected_user_path.symlink_to(chat_file.absolute())
    connected_user_path.resolve()


    print("chat file is: ", chat_file)
    append_new_message(header, chat_file)
    print(chat_file)
    
