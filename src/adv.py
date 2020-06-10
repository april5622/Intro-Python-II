import sys
from player import Player
from existingRooms import room




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


print("The Adventure Game")

player = Player("April")
player.location()
choice = None


while not choice == 'q':
    choice = input("Please choose [n], [s], [w], [e] or [q] to Quit : ")
    if len(choice.split()) == 1:
        firstChoice  = choice[0]
        if firstChoice == 'n'or firstChoice == 's' or firstChoice == 'w' or firstChoice == 'e':
            dir = firstChoice
            player.roomChange(dir)

        elif firstChoice == 'q':
            print("End of Game")
            sys.exit(1)

        else:
            print("Invalid Command")

    else: 
        print ("Invalid Command")



        