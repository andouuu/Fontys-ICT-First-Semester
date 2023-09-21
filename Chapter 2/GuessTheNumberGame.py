import random
wishToContinue=True
minAttempts=101
while wishToContinue:
    numberToGuess=random.randrange(1,100)
    yourNumber=int(input("Input your guess: "))
    count=1
    while yourNumber!=numberToGuess:
        if yourNumber not in range(1,101):
            print("Your number needs to be between 1 and 100")
            yourNumber=int(input("Input your guess: "))
            continue
        if yourNumber>numberToGuess:
            print("Too high!")
        if yourNumber<numberToGuess:
            print("Too low!")
        yourNumber=int(input("Input your guess: "))
        count+=1
    if count<minAttempts:
        minAttempts=count
    print(F"Congratulations, you won in {count} tries!!!!!!")
    print(f"Best score: {minAttempts}")
    command=input("Do you wish to continue playing?")
    if command.upper=="NO":
        wishToContinue=False
