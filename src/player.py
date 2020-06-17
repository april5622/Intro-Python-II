# Write a class to hold player information, e.g. what room they are in
# currently.

from existingRooms import room

class Player:
    def __init__(self, name, current_room = room["outside"], inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def playerInventory(self):
        if len(self.inventory) < 1:
            print("Inventory Empty")
        for i in self.inventory:
            print(f"Inventory List: {i}")
    
    # Player taking an item in the room
    def takeItem(self, item):
        stuff = None

        for i in self.current_room.items:
            if i.name == item:
                stuff = i
        
            if stuff:
                self.inventory.append(stuff)
                stuff.on_take(stuff)
                self.current_room.items.remove(stuff)
            else:
                print("Cannot take item")
        else:
            print("Item is not in this room\n")

    # Player dropping an item in the room     
    def dropItem(self, item):      
        stuff = None  

        for i in self.inventory.items:
            if i.name == item:
                stuff = i

            if stuff:
                self.inventory.remove(stuff)
                stuff.on_drop(stuff)
                self.current_room.items.append(stuff)
                # self.current_room.roomItems(self)
                # self.playerInventory()

    
    # Current location
    def location(self):
        print(f"I am currently in {self.current_room.name}")

    # Displaying the player's current location 
    def travelInfo(self, dir):
        print(f"\nYou are heading {dir} and will arrive at the {self.current_room.name}: {self.current_room.description}")

    # When picking a choice and going into a new room
    def roomChange(self, direction): 
        theWay = f"{direction}_to"

        if getattr(self.current_room, theWay):
            newRoom = getattr(self.current_room, theWay)
            self.current_room = newRoom
            self.travelInfo(direction)
            self.current_room.roomItems(self)
        else:
            print("Cannot go that way.")
            
    def __str__(self):
        return f"{self.name} is in this {self.current_room} by going {self.roomChange}"

