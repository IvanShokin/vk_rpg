#from bot import User
from random import randint
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from json import load, dump, dumps
from os.path import isfile

with open('config.json', 'r') as file:
    config = load(file)

token = config.get('token')

vk = VkApi(token=token)
longpoll = VkLongPoll(vk)


def get_button(text, color):
    return {
        'action': {
            'type': 'text',
            'payload': "{\"button\": \"" + "1" + "\"}",
            'label': str(text),
        },
        'color': str(color),
    }


def get_keyboard(list_words):
    buttons = []
    for word, color in list_words:
        buttons.append([get_button(word, color)])

    dict_keyboard = {
        'one_time': True,
        'buttons': buttons,
    }
    return str(dumps(dict_keyboard, ensure_ascii=False).encode('utf-8').decode('utf-8'))


def new_mess(user_id, mes_for_user, list_words_color):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': mes_for_user,
               'random_id': randint(0, 1000000000),
               'keyboard': get_keyboard(list_words_color)})


def save(user_save):
    with open(f'{user_save.id_user}.json', "w") as file_user:
        user_dict = {
            'health': user_save.health,
            'power': user_save.power,
            'mind': user_save.mind,
            'inventory': user_save.inventory,
            'money': user_save.money,
            'stamina': user_save.stamina
        }
        dump(user_dict, file_user)


with open('requests_response.json', 'r') as file:
    requests_response = load(file)

all_features = 'money', 'bet', 'box', 'true_answer', 'condition'
health, power, mind, inventory, money, stamina = [dict_user.get(features) for features in all_features]

user = User(event.user_id, health, power, box, mind, inventory, money, stamina)

response_mess, keyboard = user.response(event.message)
new_mess(event.user_id, response_mess, keyboard)
save(user)
