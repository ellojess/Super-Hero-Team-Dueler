import random

class Ability:
    def __init__(self, name, attack_strength):
      '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
       # Instantiate the variables listed in the docstring with then
       # values passed in
      self.name = name
      self.strength = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # Use random.randint(a, b) to select a random attack value
      # Return an attack value between 0 and the full attack.
      attack_value = random.randint(0, self.max_damage)
      # Hint: The constructor initializes the maximum attack value.
      #pass

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # Create instance variables for the values passed in
        self.name = name
        self.max_block = max_block
        # pass

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        max_block = random.randint(0, self.max_block)
        # pass

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        pass

class Hero:
    def __init__(self, name, starting_health=100):
      '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use
       # pass
       self.abilities = []
       self.armors = []
       self.name = name
       self.starting_health = starting_health
       self.current_health = current_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # Add ability object to abilities:List
        self.abilities.append(ability)
        # pass

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        # This method should run the block method on each armor in self.armors


    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        # pass

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check whether the hero is alive and return true or false
        # pass

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Print the victor's name to the screen.
        # pass

# #  test work by calling new methods
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Debugging Ability", 20)
#     # print(ability.name)
#     print(ability.attack())

# test add_ability in Hero class
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     print(hero.abilities)

# test function for is_alive
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# test to see if Hero class is working properly
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
