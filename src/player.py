# Write a class to hold player information, e.g. what room they are in
# currently.

from existingRooms import room

class Player:
    def __init__(self, name, current_room = room["outside"]):
        self.name = name
        self.current_room = current_room

    def location(self):
        print(f"I am currently in {self.current_room.name}")

    def travelInfo(self, dir):
        print(f"You are heading {dir} and will arrive at the {self.current_room.name}: {self.current_room.description}")

    def roomChange(self, direction):
        theWay = f"{direction}_to"

        if getattr(self.current_room, theWay, False):
            newRoom = getattr(self.current_room, theWay, False)
            self.current_room = newRoom
            self.travelInfo("North")
        else:
            print("Cannot go that way.")

    def traveling(self, marker):
        self.current_room = room[marker]
        self.location()
            
    def __str__(self):
        return f"{self.name} is in this {self.current_room} by going {self.roomChange}"

