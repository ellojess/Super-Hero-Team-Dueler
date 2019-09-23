import random

class Ability:
    def __init__(self, name, attack_strength):
      '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
      pass

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # Return an attack value between 0 and the full attack.
      random.randint(0, 5)
      # Hint: The constructor initializes the maximum attack value.
      pass


    #  test work by calling new methods
    if __name__ == "__main__":
        # If you run this file from the terminal
        # this block is executed.
        ability = Ability("Debugging Ability", 20)
        # print(ability.name)
        print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        pass

    def block(self): 
        ''' Return a random value between 0 and the initialized max_block strength. ''' 
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

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)