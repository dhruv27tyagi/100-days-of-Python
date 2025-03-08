import random

possible_options = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
           ['!','@','#','$','%','&','*'],
           ['1','2','3','4','5','6','7','8','9','10']]


print("Welcome to Password Generator!")

input_letters = int(input("How many letters would you like in your password?\n"))
input_symbols = int(input("How many symbols would you like?\n"))
input_numbers = int(input("How many numbers would you like?\n"))

total_letters = input_letters + input_numbers + input_symbols

password = ''

for choice in range(total_letters):
    choice = random.choice(possible_options[random.randrange(0,3)])
    password = password + choice
    


print(f"Your password is: {password}")
    



