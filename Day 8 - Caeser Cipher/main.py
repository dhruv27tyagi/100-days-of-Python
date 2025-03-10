"""
Step 1 - Take input from user

step 2 - ask for encryption or decryption

step 3 - ask for shift number 

step 4 - return results

"""
alphabets  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for alphabet in original_text:
        if alphabet in alphabets:
            alphabet = alphabets[(alphabets.index(alphabet)-shift_amount) % len(alphabets)] 
            decrypted_text = decrypted_text + alphabet   
        elif alphabet not in alphabets:
            alphabet = alphabet
            encrypted_text = encrypted_text + alphabet 

    print(f"Here is the decoded text: {decrypted_text}")

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for alphabet in original_text:
        if alphabet in alphabets:
            alphabet = alphabets[(alphabets.index(alphabet)+shift_amount) % len(alphabets)]
            encrypted_text = encrypted_text + alphabet
        elif alphabet not in alphabets:
            alphabet = alphabet
            encrypted_text = encrypted_text + alphabet

    print(f"Here is the encoded text: {encrypted_text}")

program_on = True

while program_on == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type your shift number: \n"))
    except ValueError:
        print("Please enter a valid integer only.")


    
    if direction == "encode":
        encrypt(original_text= text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text= text, shift_amount=shift)
    else:
        print("Wrong Command. Please enter encode or decode only")
    continue_program = input("Type 'yes' if you want to go again.Otherwise type 'no'\n").lower()
    if continue_program == "yes":
        program_on = True
    elif continue_program =="no":
        program_on = False
    else:
        print("Invalid input.")



