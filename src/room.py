# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n=None, s=None, w=None, e=None, items=[]):
        self.name = name
        self.description = description
        self.n_to = n
        self.s_to = s
        self.w_to = w
        self.e_to = e
        self.items = items

    # Items in room
    def roomItems(self, player):
        if player.current_room.items:
            for item in player.current_room.items:
                print(f'There is a {item.name}: {item.description}')
        else:
            print("\nNo item in this room")

        

    def __str__(self):
        return f"\nThere is a {self.name}: {self.description}"