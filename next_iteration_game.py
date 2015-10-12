import random


class Game(object):
    def __init__(self):
        self.money = 0

    def play(self):
        print self.introduction

        while True:
            print
            print self.location.description
            self.transition()

            choice = random.choice(self.location.events)
            self.money += choice.money
            print choice.message
            if self.money >= 40:
                print "You've got enough for pizza - maybe even 2! AW YEAH."
                exit(1)
            print "Pizza Money: %d" % self.money

    def transition(self):
        transitions = self.location.transitions
        print "Where do you want to go? "
        for (index, transition) in enumerate(transitions):
            print index +1, transition.title

        choice = int(raw_input("Choose a room or type 0 to exit. "))
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
Hello! Welcome to the Subway Pizza Adventure! You're Brian the cat and you love pizza!
Navigate around the Subway to find $$ to buy pizza
"""


        lobby = Place("Lobby", "You are in the lobby of the subway",
            (Event("You find a pile of trash on the floor and decide to search it. Woohoo! $5!", 5),
            Event("Notice something shiny in corner. Aw yeah, $1!", 1)))

        hallway1 = Place("Hallway1", "You are in the upstairs hallway of the subway",
            (Event("A really nice looking dude asks you for money. You give him $1.", -1),
            Event("You search the trashcan for any extra dollaz lying around. Sweet! You find $10!", 10)))

        upstairs = Place("Upstairs Platform", "You are on the upstairs platform of the subway",
            (Event("You see a backpack in the corner. $5!", 5),
            Event("There's a guy giving out free money!! Iknorite? $3",3)))

        subwayCar = Place("Subway Car", "You are in the car of the subway ",
            (Event("You see a fanny pack lying on the ground. Awesome, $5", 5),
            Event("Some older nice lookin' lady asks you for money. You give her $5", -5)))


        lobby.transitions = (hallway1,)
        hallway1.transitions = (lobby, upstairs)
        upstairs.transitions = (hallway1,subwayCar)
        subwayCar.transitions = (upstairs,)

        self.location = lobby

game = CurrentGame()
game.play()
