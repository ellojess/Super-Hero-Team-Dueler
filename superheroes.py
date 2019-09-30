import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
       # Instantiate the variables listed in the docstring with the values passed in
        self.name = name
        self.strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
      # Use random.randint(a, b) to select a random attack value
      # Return an attack value between 0 and the full attack.
        attack_value = random.randint(0, self.strength)
        return attack_value
      # The constructor initializes the maximum attack value.

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # Create instance variables for the values passed in
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # ' // ' operator to be certain that you return an integer
        return random.randint(self.strength//2, self.strength)

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
       # Initialize instance variables values as instance variables
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # Add ability object to abilities:List
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        # This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        total = 0
        for abilities in self.abilities:
            total += abilities.attack()
        return total

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self, damage_amt = 0):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        # This method should run the block method on each armor in self.armors
        total = 0

        for armor in self.armors:
            total += armor.block()
        return total

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health -= damage - self.defend()

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        while self.is_alive() and opponent.is_alive():
            self_attack = self.attack()
            opponent_attack = opponent.attack()

            opponent.take_damage(self_attack)
            self.take_damage(opponent_attack)

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("It's a tie!")
        elif self.is_alive() == False:
        # Print the victor's name to the screen.
            print(opponent.name + " won!")
            self.add_deaths(1)
            self.add_kill(1)
        else:
            print(self.name + " won!")
            self.add_deaths(1)
            opponent.add_kill(1)

    # this method that will act as a setter for self.kills
    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # This method should add the number of kills to self.kills
        self.kills += num_kills

    # this method that will act as a setter for self.deaths
    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add Armor to self.armors
            armor: Armor Object
        '''
        # This method will add the armor object that is passed in to
        # the list of armor objects defined in the constructor: `self.armors`.
        self.armors.append(armor)

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # Implement constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

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

    # view the teams heros
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)

    # add hero to team
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # Add the Hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)

    def heroes_alive(self):
        alive_heroes = []

        for hero in self.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)
        return alive_heroes

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        alive_team_one = self.heroes_alive()
        alive_team_two = other_team.heroes_alive()

        while len(alive_team_one) > 0 and len(alive_team_two) > 0:
        # Randomly select a living hero from each team
            team_one_hero = random.choice(alive_team_one)
            team_two_hero = random.choice(alive_team_two)
            # Fight each hero until a victor emerges.
            team_one_hero.fight(team_two_hero)

        # removes hero is they're no longer alive
            if not team_one_hero.is_alive():
                alive_team_one.remove(team_one_hero)
            if not team_two_hero.is_alive():
                alive_team_two.remove(team_two_hero)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.health = hero.starting_health

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

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # create instance variables named team_one and team_two that will hold our teams.
        self.team_one = Team('team_one')
        self.team_two = Team('team_two')

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        ability_name = input("Enter hero's ability: ")
        ability_value = int(input("Enter ability strength (number value): "))
        # return the new ability object.
        return Ability(ability_name, ability_value)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # This method will allow a user to create a weapon.
        weapon_name = input("Enter weapon: ")
        weapon_value = int(input("Enter weapon strength (number value): "))

        return Weapon(weapon_name, weapon_value)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # This method will allow a user to create a piece of armor
        armor_name = input("Enter armor: ")
        armor_value = int(input("Enter armor strength (number value): "))

        return Armor(armor_name, armor_value)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # This method should allow a user to create a hero.
        hero_name = input("Enter hero's name: ")
        starting_health = int(input("Enter hero's HP (number value): "))
        hero = Hero(hero_name, starting_health)
        # User should be able to specify if they want armors, weapons, and
        # abilities
        # add_abilities = input("Should your hero have abilities? (Y/n): ")
        while input("Should your hero have abilities? (Y/n): ") in "yY":
            abilities = self.create_ability()
            hero.add_ability(abilities)

        # Call the methods you made above and use the return values to build
        # your hero.
        while input("Should your hero have armor? (Y/n): ") in "yY": # "yY" same as ('y', 'yes')
            hero.add_armor(self.create_armor())

        while input("Should your hero have weapon? (Y/n): ") in "yY":
                hero.add_weapon(self.create_weapon())
        # return the new hero object
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        self.team_one = Team(input("Enter team ones name: "))

        # Prompt the user for the number of Heroes on team one
        for _ in range(int(input("How many heros are in team 1?: "))):
        # call self.create_hero() for every hero that the user wants to add to team one
            self.team_one.add_hero(self.create_hero())
            # Add the created hero to team one.
            self.team_one.view_all_heroes()

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # This method should allow a user to create team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        self.team_two = Team(input("Enter team twos name: "))

        # Prompt the user for the number of Heroes on team two
        for _ in range(int(input("How many heros are in team 2?: "))):
            # Add the created hero to team two.
            self.team_two.add_hero(self.create_hero())
            # list all heros in team
            self.team_two.view_all_heroes()

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # This method should battle the teams together.
        # Call the attack method that exists in your team objects for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # Declare winning team
        if self.team_one.heroes_alive():
            print("Team one wins the game!")
        elif self.team_two.heroes_alive():
            print("Team two wins the game!")
        else:
            print("It's a tie")
        # Show both teams average kill/death ratio.
        self.team_one.stats()
        print("--------------------")
        self.team_two.stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? (Y/n): ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False
        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
