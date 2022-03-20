import json
from random import randint

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

from bot import User, MENU

with open('config.json', 'r') as file:
    config = json.load(file)

vk = VkApi(token=config.get('token'))
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
    return str(json.dumps(dict_keyboard, ensure_ascii=False).encode('utf-8').decode('utf-8'))


def new_mess(user_id, mes_for_user, list_words_color):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': mes_for_user,
               'random_id': randint(0, 1000000000),
               'keyboard': get_keyboard(list_words_color)})


print('Start bot')
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        print(event.user_id, event.text)

        user = User(event.user_id)
        hero, new_user = user.get_hero()
        if not new_user:
            response_mess, keyboard = hero.response(event.text)
        else:
            response_mess, keyboard = 'Добро пожаловать в пошаговую, ролевую MO-RPG. Выбери действие', MENU

        user.save_hero(hero)
        new_mess(event.user_id, response_mess, keyboard)
