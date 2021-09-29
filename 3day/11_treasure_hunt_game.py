print("Welcome to treasure island!")
print("Your mission is to find treasure")
road=input("\nYou\'ar at cross road, \nwhere do you want to go? \ntype 'right' or 'left': ").lower()

if road=="left":
    lake=input("\nYou came to lake, \nThere is a island in middle of lake. \nType 'wait' for boat OR 'swim' to swim across:  ").lower()

    if lake == "wait":
        door = input("\nYou arrive at island unharmed. \nThere is a house with 3 doors. \nRed, Yellow & Blue.\nWhich colour do you choose? ").lower()
    
        if door == "blue":
            print("\nYou enter a room full of beasts. \n\t--> GAME OVER <-- ")
        elif door == "red":
            print("\nYou enter room full of fire. \n\t--> GAME OVER <--")
        elif door == "yellow":
            print("\nYou find the treasure.\n \t-->YOU WIN <--")
        else:
            print("\nYou choose a door that does not exist.\n\t--> GAME OVER <--")
    
    else:
        print("\nYou attacked by crocodile. \n\t--> GAME OVER <-- ")

else:
    print("\nYou had an accident, dies. \n\t--> GAME OVER <--")