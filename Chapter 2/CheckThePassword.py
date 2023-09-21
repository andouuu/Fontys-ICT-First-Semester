prePass="Banana"
isPassCorrect=False
for i in range(3):
    tryPass=input("Enter password: ")
    if tryPass==prePass:
        print("Password correct!")
        isPassCorrect=True
        break
    else:
        print("Password incorrect!")
if not isPassCorrect:
    print("Your account has been blocked!")