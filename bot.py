from random import randint

menu = ['1 - Поиск игры по сети',
        '2 - Зафармить локу',
        '3 - Продать вещи',
        '4 - Просмотреть инвент',
        '5 - Просмотреть колличество денег',
        '6 - Просмотреть фулл характеристику перса']

objects = ['sword',
           'shield',
           'health potion',
           'power potion',
           'mind potion',
           'knife']


class Hero:
    def __init__(self, health, power, mind, inventory, money, stamina):
        self.health = health
        self.power = power
        self.mind = mind
        self.inventory = ['knife']
        self.money = 100
        self.stamina = 100

    def farming(self, inventory, health, power, stamina):
        self.add_object(inventory)
        self.health_2(health)
        self.power_2(power)
        self.stamina_2(stamina)

    def add_object(self, inventory):
        for i in objects:
            random_object = randint(0, 4)
            inventory.append(random_object)

    def health_2(self, health):
        health -= randint(1, 50)

    def power_2(self, power):
        power += randint(1, 50)

    def stamina_2(self, stamina):
        stamina -= randint(1, 20)


# def sell(money):


if __name__ == '__main__':
    hero = Hero(100, 50, 200)
    hero.farming(45, 45, 870, 90)