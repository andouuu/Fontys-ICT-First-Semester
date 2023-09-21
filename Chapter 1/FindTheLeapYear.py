year=int(input("Type a year of your choice: "))
leapYear="The year is leap year!"
notLeapYear="The year is not a leap year!"
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(leapYear)
        else:
           print(notLeapYear)
    else:
        print(leapYear)
else:
    print(notLeapYear) 