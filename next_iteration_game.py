from random import random


class Game(object):
    def __init__(self):
        self.money = 0

    def play(self):
        print self.introduction

        while True:
            print
            print self.location.description
            self.transition()

            for event in self.location.events:
                self.money += event.process()
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
    def __init__(self, probability, message, money):
        self.probability = probability
        self.message = message
        self.money = money

# TODO something is broken here but i have no idea what!
# error == self.money += event.process() TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'
    def process(self):
        if random() > self.probability:
            print self.message
            return self.money
        elif random() < self.probability:
            return 0
            print "Sorry, there's nothing here!"

class CurrentGame(Game):
    def __init__(self):
        super(CurrentGame, self).__init__()
        self.introduction = """
Hello! Welcome to the Subway Pizza Adventure! You're Brian the cat and you love pizza!
Navigate around the Subway to find $$ to buy pizza
"""


        lobby = Place("Lobby", "You are in the lobby of the subway",
            (Event(0.5, "You find a pile of trash on the floor and decide to search it. Woohoo! $5!", 5),
            Event(0.5, "Notice something shiny in corner. Aw yeah, $1!", 1)))

        hallway1 = Place("Hallway1", "You are in the upstairs hallway of the subway",
            (Event(0.5, "A really nice looking dude asks you for money. You give him $1.", -1),
            Event(0.5, "You search the trashcan for any extra dollaz lying around. Sweet! You find $10!", 10)))

        upstairs = Place("Upstairs Platform", "You are on the upstairs platform of the subway",
            (Event(.5, "You see a backpack in the corner. $5!", 5),
            Event(.5, "There's a guy giving out free money!! Iknorite? $3",3)))

        subwayCar = Place("Subway Car", "You are in the car of the subway ",
            (Event(.5, "You see a fanny pack lying on the ground. Awesome, $20", 5),
            Event(.5, "Some older nice lookin' lady asks you for money. You give her $5", -5)))


        lobby.transitions = (hallway1,)
        hallway1.transitions = (lobby, upstairs)
        upstairs.transitions = (hallway1,subwayCar)
        subwayCar.transitions = (upstairs,)

        self.location = lobby

game = CurrentGame()
game.play()
