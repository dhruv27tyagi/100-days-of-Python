## Assume infinite deck
## Ace can be 1 or 11 depending on current sum and when it is drawn

import random

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
game_on = True

def sum(list):
    sum = 0
    for number in list:
        sum = number + sum
    return sum

def check_21(user_cards, dealer_cards):
    if sum(user_cards) == 21:
        print("User Won!")
        game_on = False
    elif sum(dealer_cards) == 21:
        print("Computer Won!")
        game_on = False
    elif sum(user_cards) == sum(dealer_cards) == 21:
        print("both got 21. Comp Wins")
        game_on = False
    else:
        pass

def comp_draws_card(cards):
    if sum(cards) < 17:
        cards.append(random.choice(cards))
    else:
        cards = cards

    return cards

def check_score(user_cards, dealer_cards):

    if sum(user_cards) > 21:
        print("You lost.")

    elif sum(user_cards) > sum(dealer_cards):
        print(f"The computer got {dealer_cards} cards")
        print("You Won!")
            
    elif sum(dealer_cards) > sum(user_cards):
        print(f"The computer got {dealer_cards} cards")
        print("The dealer won")

    elif sum(user_cards) > sum(dealer_cards):
        print(f"The computer got {dealer_cards} cards")
        print("The player won")

    

while game_on:
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game == "y":
        game_on = True

## Task 1 - Randomly assign two cards to the user and display sum of the cards. Also display computers' first card
    
        user_cards = random.choices(cards, k = 2)  ## two cards assigned to the player
        dealer_cards = random.choices(cards, k = 2) ## two cards assigned to the computer

        print(f"You have drawn the following cards: {user_cards}. Your total is {sum(user_cards)}") # display player cards and sum
        print(f"first card of the computer is: {dealer_cards[0]}") # display first card of computer

        check_21(user_cards=user_cards,dealer_cards=dealer_cards) ## check if anyone has a 21 or not

        another_card = input("Do you want to draw another card? Type 'y' or 'n': ") ## ask user to draw another card
        
        if another_card == "y":
            user_cards.append(random.choice(cards)) ## assign a third card to the user

            print(f"Your cards are {user_cards}. Your sum is {sum(user_cards)}") 

            print(comp_draws_card(cards=dealer_cards))
            check_21(user_cards=user_cards,dealer_cards=dealer_cards)
            check_score(user_cards=user_cards,dealer_cards=dealer_cards)## display the user cards and sum

        elif another_card == "n":
            comp_draws_card(cards=dealer_cards)
            check_score(user_cards=user_cards,dealer_cards=dealer_cards)

    else:
        game_on = False
