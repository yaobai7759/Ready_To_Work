import re, os


class Hero(object):
    """
    英雄
    """

    def __init__(self, nick_name, life_value, attack_info):
        self.nick_name = nick_name
        self.life_value = life_value
        self.attack_info = attack_info

    def attack(self, atk_obj):
        atk_obj.life_value -= self.attack_info
        if atk_obj.life_value <= 0:
            print("%s is died" % atk_obj.nick_name)


class Riven(Hero):
    pass


class GuyLun(Hero):
    pass


r = Riven('rll', 100, 150)
g = GuyLun('g11', 100, 100)

r.attack(g)
