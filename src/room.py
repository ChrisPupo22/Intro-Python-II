#Part I
# Implement a class to hold room information. This should have name and
# description attributes.

#Part II
# Add the ability to add items to rooms.
# The Room class should be extended with a list that holds the Items that are currently in that room.
# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.


class Room: 
    def __init__(self, room_name, room_desc):
        self.room_name = room_name
        self.room_desc = room_desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = []

    def __str__(self):
        #string method that will print when room is called
        return f"{self.room_name}\n\n{self.room_desc}"
        


