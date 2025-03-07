print("Welcome to Treasure Island")
print("Your mission is to find the tresure")
direction = input("You've come across a road. Where do you want to go? 'left' of 'right'?\n").lower()

if direction == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across \n").lower()
    if lake == "wait":
        colour = input("You arrive at the island unharmed. There is a house with three doors. \nOne red, one yellow and one blue. which colour do you choose? \n").lower()
        if colour == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")


