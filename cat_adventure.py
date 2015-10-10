
print """

B R I A N thecat <3s P I Z Z A
a triva adventure game about a cat that's just trying to get some pizza.


HOW TO PLAY:
_____________________________________________________________
_____________________________________________________________
you are brian the cat.                                    | |
you are a cat that loves pizza.                           | |
your mission; search the subway for $$.                   | |
use your $$ to buy brian the cat pizz!                    | |
_____________________________________________________________
_____________________________________________________________

GAME COMMANDS:
_____________________________________________________________
_____________________________________________________________
                                                          | |
these will be the game commands!                          | |
_____________________________________________________________
_____________________________________________________________

MAP:

this will be the map!

"""

class Room(object):
    def __init__(self,name,greeting,objects):
        self.name = name
        self.greeting = greeting
        self.objects = objects

lobby = Room("Lobby", "Hello! You are in the LOBBY!",{"backpack": 10,"trashcan": 2})
hallway1 = Room("Hallway1", "Hello! You are in HALLWAY1", {"floor_trash":5,"trashcan":10})
hallway2 = Room("Hallway2", "Hello! You are in HALLWAY2", {"bag":5,"floor":0})
upstairs_platform = Room("Upstairs Platform", "Hello! You are on the UPSTAIRS PLATFORM",{"bag":10,"backpack":40})
downstairs_platform = Room("Dowstairs Platform", "Hello! You are on the DOWNSTAIRS PLATFORM", {"trashcan":10, "person_sleeping":100})
subway_car = Room("Subway Car", "Hello! You are in the SUBWAY CAR", {"seat":10, "floor":15})
