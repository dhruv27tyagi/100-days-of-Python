import random

celeb_followers = {"Kohli":100,"sachin":30,"SRK":90,"jackie chan":70,"the weekend":80,"shakira":85}

print("Welcome to Higher Lower Game. Today we will be comparing the number of followers of famous celebrities")

game_on = True
current_score = 0


while game_on == True:

    keys = list(celeb_followers.keys())
    celeb_1 = random.choice(keys)
    keys.remove(celeb_1)
    celeb_2 = random.choice(keys)
    followers_of_celeb_1 = celeb_followers[celeb_1]
    followers_of_celeb_2 = celeb_followers[celeb_2]
    
    print(f"Compare A: {celeb_1} with B: {celeb_2}")
    #print(followers_of_celeb_1,followers_of_celeb_2)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == "a" and followers_of_celeb_1>followers_of_celeb_2:
        print("Correct.")
        current_score += 1
        print(f"Your Score is: {current_score}")

    elif guess == "a" and followers_of_celeb_1<followers_of_celeb_2:
        print("Wrong")
        print(f"Your Score is: {current_score}")
        game_on = False

    elif guess == "b" and followers_of_celeb_2 > followers_of_celeb_1:
        print("Correct.")
        current_score += 1
        print(f"Your Score is: {current_score}")   

    elif guess == "b" and followers_of_celeb_2 < followers_of_celeb_1:
        print("Wrong")
        print(f"Your Score is: {current_score}")
        game_on = False
