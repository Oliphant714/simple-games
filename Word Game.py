secret = "dragon"
guess = "balderdash"
hint = ""
password = 'balderdash'

print("Welcome to the Word Game!")

while password.lower() == guess.lower():
    count = 5
    print(f'You have {count} gueses remaining!')
    for letter in secret:
        hint += '_ '
    print(f'Your hint is: {hint}')

    while guess.lower() != secret and count > 0:
        count -= 1
        guess = input("What is the secret word?  ")
        if len(guess) == len(secret):
            if guess.lower() != secret:
                print("Your hint is: ", end=" ")
                for index, letter in enumerate(guess): 
                    if letter.lower() == secret[index]:
                        print(letter.upper(), end=" ") 
                    elif letter.lower() in secret:
                        print(letter.lower(), end=" ")
                    else:
                        print("_", end=" ")
                print('')
        else:
            print('Your guess must have the same number of letters as the secret word.')
        if count > 0:
            print(f'You have {count} gueses remaining!')
        else:
            print('You are out of guesses.')

    if guess.lower() == secret and count >= 0:
        print(f"That is correct!  The secret word is {secret.upper()}!  You get {count*10} points!")
    else:
        print("I'm sorry but you lose.", end="  ")
        password = input('Do you have a password to get more guesses?  ')
        print("")
        hint = ""
print("Game over.  Please play again!")