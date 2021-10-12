import random

class Dragon:
    # Class variables
    hoard = [] # List of items that all dragons will hoard total

    # Fire breathing - shape of fire (balls, streams), elemental type, color, height, health, etc.
    def __init__(self, element, color, hgt, health, strength):
        self.element_type = element
        self.color = color
        self.height = hgt
        self.health = health # Current health
        self.max_health = health # Maximum health
        self.strength = strength
        self.own_hoard = [] # Dragon has no items in its own individual hoard

    # Fly, breathe fire (with fireballs or something similar), attack (another dragon)
    # Do damage of some sort
    def breathe_fire(self, other_dragon):
        print("RAWRRRRR!!!!!!")
        print(f"{self.color} breath!")
        if other_dragon.health > 10:
            other_dragon.health -= 10
            print(f"Dragon whose color is {other_dragon.color} and whose element is {other_dragon.element_type} has lost 10 HP")
        elif other_dragon.health >= 0:
            other_dragon.health = 0
            print("The other dragon has been KO'd")
        else:
            print("The other dragon is gone - no need to attack")
        return self

    def sleep(self):
        # Imagine you have 70 health and the max is 100 health - so you'd add 20% of 100, or 20, to your health
        self.health += 0.2 * self.max_health # Add 20% of the max health to the dragon's current health
        if self.health >= self.max_health: # If current health is above max health, cap it accordingly
            self.health = self.max_health
        # An alternate way to do this
        # self.health = min(self.max_health, self.health + 0.2*self.max_health)
        return self

    # Take an item randomly from the hoard
    def add_to_own_hoard(self):
        if len(Dragon.hoard) <= 0:
            print("Nothing to take")
            return self
        random_index = random.randint(0,len(Dragon.hoard)-1)
        new_item = Dragon.hoard[random_index]
        self.own_hoard.append(new_item) # Adds the item to the individual dragon's hoard
        Dragon.hoard.remove(new_item) # Removes the item from the collective hoard
        print(f"The {self.color} dragon took {new_item}")
        return self
    
    @classmethod
    def hoard_new_item(cls, new_item):
        cls.hoard.append(new_item) # Note cls.hoard here vs. Dragon.hoard above!
        return cls

# Defining instances of dragons
red_dragon = Dragon("fire","red",10.5,100,100)
blue_dragon = Dragon("water","blue",7,80,70)

print(blue_dragon.health)
red_dragon.breathe_fire(blue_dragon).sleep()
print(blue_dragon.health)
print(red_dragon.health)

Dragon.hoard_new_item("gold").hoard_new_item("magic beads").hoard_new_item("pearls")
print(Dragon.hoard)

blue_dragon.add_to_own_hoard().add_to_own_hoard().add_to_own_hoard().add_to_own_hoard()
print(Dragon.hoard)