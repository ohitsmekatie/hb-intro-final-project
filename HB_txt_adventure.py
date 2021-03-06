import random

import os, sys, inspect

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"colorama")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from colorama import init
init()

from colorama import Fore, Back, Style

# TODO add pizza method  store at the end of game
# TODO you need to fix what happens when people press a # that's not 1 or 2!
# TODO style that shit, yo!
# TODO do you want to try to add probability?
# TODO what about adding some bad guys?

# the start of the pizza shop
# def pizza_store():
#     print """
#     You have magically been transformed to Spak Brothers Pizza in Pittsburgh, PA.
#     It's seriously your lucky day. TRUST ME.
#
#     MENU:
#     1. Pizza, $10
#     2. Pizza with topping, $15
#     3. Seitan BBQ sub, $10
#     4. Coke, $2
#     5. Fries, $5
#     6. Fries with cheese, $9
#     7. Salad, $10
#     """
#     response = raw_input("What would you like get? You have %i to spend") % (self.money)

class Game(object):
    def __init__(self):
        self.money = 1

    def play(self):
        print (Fore.YELLOW + self.introduction + Fore.RESET)

        while True:
            print
            print (Fore.MAGENTA + self.location.description + Fore.RESET)
            self.transition()

            choice = random.choice(self.location.events)
            self.money += choice.money
            print (Fore.MAGENTA + choice.message + Fore.RESET)
            if self.money >= 40:
                print (Fore.YELLOW +"\n\nYou've have $%i! You definitely have enough for a pizza - MAYBE EVEN 2! " + Fore.RESET) % (self.money)
                exit(1)
            print (Fore.GREEN + "Pizza Money: %d" % self.money + Fore.RESET)

    def transition(self):
        transitions = self.location.transitions
        print (Fore.BLUE + "Where do you want to go? " + Fore.RESET)
        for (index, transition) in enumerate(transitions):
            print index +1, transition.title

        choice = int(raw_input(Fore.BLUE + "Choose a room or type 0 to exit. " + Fore.RESET))
        if choice == 0:
            exit(0)
        else:
            self.location = transitions[choice -1]

class Place(object):
    def __init__(self, title, description, events):
        self.title = title
        self.description = description
        self.events = events

class Event(object):
    def __init__(self, message, money):
        self.message = message
        self.money = money

class CurrentGame(Game):
    def __init__(self):
        super(CurrentGame, self).__init__()
        self.introduction = """
_____________________________________________________________________________________
_____________________________________________________________________________________

Hello! Welcome to the Subway Pizza Adventure! You're Brian the cat and you love pizza!

_____________________________________________________________________________________
_____________________________________________________________________________________


||==================================================||
||==================================================||
||Navigate around the Subway to find $$ to buy pizza||
||==================================================||
||==================================================||
"""


        lobby = Place("Lobby", "You are in the lobby of the subway",
            (Event("You find a pile of trash on the floor and decide to search it. Woohoo! $5!", 5),
            Event("You notice something shiny in corner. Aw yeah, $1!", 1),
            Event("$10 magically drops into your hand from the ceiling!", 10)))

        hallway1 = Place("Hallway1", "You are in the upstairs hallway of the subway",
            (Event("A really nice looking dude asks you for money. You give him $1.", -1),
            Event("You search the trashcan for any extra dollaz lying around. Sweet! You find $10!", 10),
            Event("You see a book lying on the floor. Inside of it is $3! YAY!", 3)))

        upstairs = Place("Upstairs Platform", "You are on the upstairs platform of the subway",
            (Event("You see a backpack in the corner. $5!", 5),
            Event("There's a guy giving out free money!! Iknorite? $3",3),
            Event("You got robbed. Sad panda", -2)))

        subwayCar = Place("Subway Car", "You are in the car of the subway ",
            (Event("You see a fanny pack lying on the ground. Awesome, $30", 30),
            Event("Some older nice lookin' lady asks you for money. You give her $5", -5),
            Event("You look around the floor and find...nothing. Sorry bout it!",0)))


        lobby.transitions = (hallway1,)
        hallway1.transitions = (lobby, upstairs)
        upstairs.transitions = (hallway1,subwayCar)
        subwayCar.transitions = (upstairs,)

        self.location = lobby

game = CurrentGame()
game.play()
