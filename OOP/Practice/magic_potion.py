import random

class Player(object):

    def __init__(self, name: str, health: int = 100, has_potion: bool =True):
        self.name =name
        self.health = health
        self.has_potion = has_potion

    def __str__(self):
        return f'{self.name} HP: {self.health}, Has Potion: {self.has_potion}'

    def reduce_health_by(self, amount):
        self.health = self.health - amount
        print(f'{self.name} get {amount} damage, and the HP decreased to: {self.health}')

    def drink_potion(self):
        if self.has_potion is True:
            self.health = 100
            self.has_potion = False
            print('Potion consumed.')
        else:
            print('No more Health Potion.')

    def turn(self):
        self.reduce_health_by(random.randrange(20, 50))
        if 0 < self.health < 10:
            self.drink_potion()
        if self.health <= 0:
            print('You Died!')
            return True
        return False


kryssz = Player('Kryssz')
for i in range(5):
    if kryssz.turn():
        break
else:
    print('Survived all the turns!')

