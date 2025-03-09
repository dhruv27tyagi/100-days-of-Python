import random

words = ['python','transformer','optimizer','compiler','algorithms','coding','database','cloud','gradient','regression','classification','vision','network','interpreter']

word_to_guess = random.choice(words)

lives = 6

word = ''
for i in range(len(word_to_guess)):
    word = word + '_'
      
print("Welcome to Hangman!")
print(f"Word to Guess -- {word}")

game_over = False
correct_letters = []


while not game_over:
    guess = input("Guess a letter: ")

    display = ""

    for letter in word_to_guess:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
            
        else:
            display += "_"


    print(display)  

    if guess not in word_to_guess:
        lives -= 1
        print(f"lives remaining - {lives}/6")
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("")



