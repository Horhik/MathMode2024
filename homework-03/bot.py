from database import append_new_message, get_chat_file
import json


BOT_COMMANDS = {
    'help': '<h1>ты ничего не можешь</h1> <br><br><br> <small>ask orwell about /commands</small>',
    'помоги': 'ты ничего не можешь',
    'спой': '<iframe width="420" height="345" src="https://yewtu.be/embed/i9AHJkHqkpw?autoplay=1" frameborder="0" allowfullscreen></iframe>',
    'пустота': "<q><i>Сараха сказал: «Кто живет в состоянии пустоты, лишенной сострадания, тот не открыл высшего пути; но также тот, кто медитирует только на сострадание, останется в сансаре и не достигнет освобождения».</i></q>",
    'gpt': "<h3 color='red'>Не прибегай к темным силам, будь собой</h3>",
    'commands': "<code>/help</code><br><code>/помоги</code><br><code>/спой</code><br><code>/help</пустота><br><code>/help</gpt><br><code>/display [link to image] </code> - will display an image ",
    'display': ''
    
    }
def call_orwell(username, chat, command='', message=''):

    print("CALLING BOT", message)
    if command == 'display':
        
        orwell_answer(f"<img class='image' src='{message[0]}'/>", username, chat)
    if command in BOT_COMMANDS:
        print("HELP HELP HELP")
        orwell_answer(BOT_COMMANDS[command], username, chat)


def bot_answer(text, username, chat):
    message = json.dumps({"time": 'out of time. the message are out of the bounds of this world', "sender": 'Orwell\'s eye', "text": text})
    append_new_message(message, get_chat_file(username, chat))



def orwell_answer(message, username, chat):
    bot_answer(message, username, chat)

    
