from os import walk, makedirs
from pathlib import Path

USER_FOLDER = 'users'
POOL_FILE   = 'data/pool.json'
DATA_FOLDER = 'data'

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

    #Create messages folder
    user_messages = Path(USER_FOLDER, name, 'messages')
    user_messages.mkdir(exist_ok=True, parents=True)

    #Symlink pool to messages
    user_pool = Path(user_messages, "pool.json").absolute()
    user_pool.symlink_to(pool)
    user_pool.resolve()


def create_user(name):
    name = name.lower()
    makedirs(f'{USER_FOLDER}/{name}')
    setup_user(name)

def get_chat_list(name):
    return list(map(lambda x: x.name, Path(USER_FOLDER, name, "messages").iterdir()))
