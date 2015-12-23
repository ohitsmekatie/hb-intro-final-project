# first practice to create rooms you can move around in
# this is an inifite loop!

lobby = ("Lobby", "The subway station's lobby. ")
platform1 = ("Upstairs Platform", "The upstairs platform of the subway station")
platform2 = ("Downstairs Platform", "The downstairs platform of the subway station")
subwayCar = ("Subway Car", "A subway car")

transitions = {
    lobby: (platform1,),
    platform1: (lobby, platform2),
    platform2: (platform1, subwayCar),
    subwayCar: (platform2,)
}

location = lobby

while True:
    print location[1]
    print "You can go to these places: "

    for (i, t) in enumerate(transitions[location]):
        print i + 1, t[0]

    choice = int(raw_input("Choose a number: "))
    location = transitions[location][choice - 1]
