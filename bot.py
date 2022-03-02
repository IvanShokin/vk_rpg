from random import randint

menu = ['1 - Поиск игры по сети',
        '2 - Зафармить локу',
        '3 - Продать вещи',
        '4 - Просмотреть инвент',
        '5 - Просмотреть колличество денег',
        '6 - Просмотреть фулл характеристику перса']

items = ['sword',
         'shield',
         'health potion',
         'power potion',
         'mind potion',
         'knife']


class Hero:
    def __init__(self, health, power, mind, inventory=['knife'], money=100, stamina=100):
        self.health = health
        self.power = power
        self.mind = mind
        self.inventory = inventory
        self.money = money
        self.stamina = stamina

    def farming(self):
        if self.stamina > 0:
            self.add_item()

    def add_item(self):
        new_item = items[randint(0, 5)]
        self.inventory.append(new_item)
        return new_item


if __name__ == '__main__':
    hero = Hero(100, 50, 200)
    hero.farming()
    print(hero.inventory)
