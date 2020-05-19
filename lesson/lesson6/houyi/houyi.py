# !/usr/bin/python env
# _*_ coding:utf-8 _*_
from lesson.lesson6.game.game import Game


class HouYi(Game):
    ##如果子类中重新定义了__init__，那么父类中的__init__会被覆盖
    def __init__(self):
        super().__init__(1000,200)
        self.defense = 100

    def houyi_fight(self,enemy_hp,enemy_power):
        print("我方初识血量" + str(self.hp) + "   对方初识血量" + str(enemy_hp))
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print("我方血量" + str(self.hp) + "    对方血量" + str(enemy_hp))
            if self.hp <=0:
                print("我输了")
                break
            elif enemy_hp<=0:
                print("我赢了")
                break

hp = 1000
power = 200
houyi = HouYi()
houyi.houyi_fight(hp,power)