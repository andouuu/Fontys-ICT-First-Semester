cmd="J";
while cmd.capitalize=="J":
    number=int(input("Type a number from 1 to 9:"));
    if number>=10:
        print("You violate the rules of the game!");
    elif number==9:
        print("You win!");
    else:
        print(str(number) + " I win!")
    cmd=input("Do you want to play another game? J/N")
