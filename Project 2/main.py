import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1

    if(userGuess == randNumber):
        print("You have guessed it right!")
    else:
        if(userGuess > randNumber):
            print("You have guessed it wrong! Enter a smaller number")
        else:
            print("You have guessed it wrong! Enter a larger number")

print(f"You have guessed the number in {guesses} guesses")

with open("hiscore.txt") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("You have just broken the hiscore")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))