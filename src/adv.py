from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'Mjolnir': Item("The Mjolnir", 
                """The most powerful weapon in the galaxy, too bad you can't pick it up """),
                    
    'Basket': Item("Basket of apples ",
                """feel free to replenish yourself with these random apples, who knows if they're poisonous or not..."""),

    'Fishing pole': Item("The great fishing pole",
                """If you manage to get this fishing pole out of these caves you will be granted the ability to catch unlimited fish!"""),

    'Knights Sword': Item("The Knights Sword",
                """Seems as though a Knight came through the caves and lost his trusty sword, I would recommend picking it up! """)

}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player(input('What is your name?'), room['outside'])

print(f"Hello, {p1.name}\n\n{p1.current_room}")


#commands = input("Please enter a direction: 'n', 's', 'e', 'w' or click 'q' to quit. ")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


    #Print current room and current description 
# print('You are currently '+ p1.current_room +'')

# player_cmd = input("Please enter a direction: 'n', 's', 'e', 'w' or click 'q' to quit. ")

# directions = ['n', 's', 'e', 'w']

while True: 
    print(p1.current_room)
    cmd = input("->").lower()
    if cmd in ["n", "s", "e", "w"]:
        #Move to that room
        current_room = p1.current_room
        next_room = getattr(current_room, f"{cmd}_to")
        if next_room is not None: 
            p1.current_room = next_room
        else: 
            print("You cannot move in that direction")
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else: 
        print("I did not understand that command")







