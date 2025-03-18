class Character:
    def __init__(self, inHealth=0, inAttack=0, inSpeed=0, inDefense=0):
        self.health = inHealth
        self.attack = inAttack
        self.speed = inSpeed
        self.defense = inDefense
        

class Item:
    def __init__(self, inValue=0, inStatType="", inCooldown=0, inQuantity=0):
        self.value = inValue
        self.statType = inStatType
        self.cooldown = inCooldown
        self.quantity = inQuantity

class Player(Character):
    def __init__(self, inHealth=0, inAttack=0, inSpeed=0, inDefense=0, inItems=[]):
        super().__init__(inHealth, inAttack, inSpeed, inDefense)
        self.items = inItems

class Enemy(Character):
    def __init__(self, inHealth=0, inAttack=0, inSpeed=0, inDefense=0):
        super().__init__(inHealth, inAttack, inSpeed, inDefense)






def main():



main()