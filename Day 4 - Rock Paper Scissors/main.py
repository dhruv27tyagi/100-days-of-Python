import random 
options = [0,1,2]


input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.choice(options)
#print(computer_choice)

if input == computer_choice:
    print("Draw")
elif computer_choice == 0 and input == 1:
        print("the computer chose Rock. You won!")
elif computer_choice == 0 and input ==2:
        print("The computer chose Rock. You lost.")
elif computer_choice == 1 and input == 0:
        print("The computer chose Paper. You lost.")
elif computer_choice == 1 and input == 2:
        print("The computer chose Paper. You Win!")
elif computer_choice == 2 and input == 0:
        print("The computer chose Scissors. You Won!")
elif computer_choice == 2 and input == 1:
        print("The computer chose Scissors. You lost.")
