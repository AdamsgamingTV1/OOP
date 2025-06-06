import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword, spider_trident


hero = Hero(name="Hero", health="100")
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health="200")

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
