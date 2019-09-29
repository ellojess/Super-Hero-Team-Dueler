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
      # The constructor initializes the maximum attack value.
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
        # ' // ' operator to be certain that you return an integer
        attack_value = random.randint(self.strength//2, self.strength)
        return attack_value
        # pass // double check this / needs testing

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # Implement constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []
        # pass

    # find and remove from the team's list of Heroes
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return 1
        return 0
        # pass

    # view the teams heros
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)
        # pass

    # add hero to team
    def add_hero(self, hero)
      '''Add Hero object to self.heroes.'''
      # Add the Hero object that is passed in to the list of heroes in
      # self.heroes
      self.heroes.append(hero)
      # pass

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        team_one = []
        team_two = []


        # pass

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.health = hero.starting_health
        # pass

    def stats(self):
        '''Print team statistics'''
        # This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Used the information stored in each hero.
        for hero in self.heroes:
            print("Hero: " + hero.name)
            print("Kills: " + str(hero.kills))
            print("Deaths: " + str(hero.deaths))
        # pass

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
       self.deaths = 0
       self.kills = 0

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
        total_armor = 0

        for armor in self.armors:
            total_armor += hero.block()
        return total_armor

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health = damage - self.defend()
        # pass // double check this


    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else:
            return False
        # pass

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # Fight each hero until a victor emerges.
        # Print the victor's name to the screen.

        # Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight

        while self.is_alive() and opponent.is_alive():

            self_attack = self.attack()
            opponent_attack = opponent.attack()

            opponent.take_damage(self_attack)
            self.take_damage(opponent_attack)


        if self.abilities == [] or opponent.abilities == []:
            print("It's a tie!")
        elif self.is_alive() == False:
            print(opponent.name + " won!")
        else:
            print(self.name + " won!")

        # pass

    # this method that will act as a setter for self.kills
    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # This method should add the number of kills to self.kills
        self.kills += num_kills
        # pass

    # this method that will act as a setter for self.deaths
    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
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
