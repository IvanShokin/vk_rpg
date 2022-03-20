import json
from random import randint
from os.path import isfile

MENU = [('Фармить', 'positive'),
        ('Просмотреть инвентарь', 'secondary'),
        ('Просмотреть снаряжение', 'primary'),
        ('PvP', 'negative'),
        ('Магазин', 'primary'),
        ('Гильдия', 'primary')]


class Hero:
    def __init__(self,
                 health: int = 100,
                 power: int = 10,
                 intelligence: int = 10,
                 energy: int = 100,
                 money: int = 1000,
                 inventory=None,
                 condition: str = "menu"):
        # TODO refactor
        if inventory is None:
            inventory = []
        self.health = health
        self.power = power
        self.intelligence = intelligence
        self.energy = energy

        self.money = money
        self.inventory = inventory

        self.condition = condition

    def menu(self, action):
        pass

    def farm(self):
        pass

    def pvp(self):
        pass

    def response(self, new_mess: str):
        actions = {
            'menu': self.menu,
            'farm': self.farm,
            'pvp': self.pvp,
        }

        actions.get(self.condition)(new_mess)


class User:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def save_hero(self, hero: Hero):
        with open(f'{self.user_id}.json', "w") as data:
            user_dict = {
                'health': hero.health,
                'power': hero.power,
                'intelligence': hero.intelligence,
                'energy': hero.energy,
                'money': hero.money,
                'inventory': hero.inventory,
            }
            json.dump(user_dict, data)

    def get_hero(self):
        file_name = f'{self.user_id}.json'
        if isfile(file_name):
            with open(file_name, "r") as data:
                data = json.load(data)
                return Hero(
                    health=data.get('health'),
                    power=data.get('power'),
                    intelligence=data.get('intelligence'),
                    energy=data.get('energy'),
                    money=data.get('money'),
                    inventory=data.get('inventory'),
                ), False
        else:
            return Hero(), True
