# Write your code here
import random

class Hero():

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    potions = 1

    def attack(self, target):
        print("the hero attacked and did " + str(self.damage) + " damage")
        target.health -= self.damage

    def heal(self):
        self.health += 5
        self.potions -= 1


    def die(self):
        print("the hero died\n\nyou lose")
  
class Monster(): 
    
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def attack(self, target):
        randnum = random.randrange(0,100)
        if randnum < 90:
            target.health -= self.damage
            print("the monster attacked and did " + str(self.damage) + " damage")

    def runAway(self):
        print("the monster ran away\n\nyou win")

    def roar(self):
        print("the monster roared")

stat_total = random.randrange(50, 80)
print("stat total: " + str(stat_total))
print("attack and health have to add up to stat total")
h_attack = input("attack:")
h_health = input("health:")

while True:
    if int(h_attack) + int(h_health) == stat_total:
        hero = Hero(int(h_health), int(h_attack))
        break
    else:
        print("error: attack and health have to add up to stat total")
        h_attack = input("attack:")
        h_health = input("health: ")
        
m_attack = random.randrange(5, 10)
m_health = random.randrange(50, 100)

monster = Monster(m_health, m_attack)

while True:
    print("hero health: " + str(hero.health))
    print("monster health: " + str(monster.health))

    while True:
        print("moves:\nattack\nhealing potion") 
        move = input("move:")
        if move == "attack":
            hero.attack(monster)
            break
        elif move == "heal" and hero.potions > 0:
            hero.heal()
            break
        else:
            print("no potions left")

    m_moves = ["roar", "attack", "attack", "attack", "attack"]
    if m_moves[random.randrange(0,len(m_moves))] == "attack":
        monster.attack(hero)
    else:
        monster.roar()
    
    if hero.health <= 0:
        hero.die()
        break

    if monster.health <= 1:
        monster.runAway()
        break
    










