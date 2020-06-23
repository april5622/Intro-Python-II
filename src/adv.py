import sys
from player import Player
from existingRooms import room
from existingItems import item




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


print("\nThe Adventure Game\n")

player = Player("April") 
choice = None

# display currently player's location and what is in the room
player.location()
player.current_room.roomItems(player)
player.playerInventory()


while not choice == 'q':
    choice = input("\nPlease go [n], [s], [w], [e] or [q] to Quit \nOr take/get or drop item: ").strip()
    # one word for parser
    if len(choice.split()) == 1:
        firstChoice = choice[0]
        if firstChoice == 'n'or firstChoice == 's' or firstChoice == 'w' or firstChoice == 'e':
            dir = firstChoice
            player.roomChange(dir)

        elif firstChoice == 'q':
            print("\nEnd of Game")
            sys.exit(1)

        else:
            print("Invalid Command")

    # two word for parser

    elif len(choice.split()) == 2:
        choice = choice.split()

        # takes first letter of a verb
        verb = choice[0][0]
        # takes item which is the second word
        noun = choice[1]

        # get or take
        if verb == 'get' or 'take':
            player.takeItem(noun)
            player.playerInventory()
 
        # drop
        elif verb == 'drop':
            player.dropItem(noun)
            player.playerInventory()

        else: 
            print("Invalid Command")
            

    else: 
        print ("Invalid Command")



        