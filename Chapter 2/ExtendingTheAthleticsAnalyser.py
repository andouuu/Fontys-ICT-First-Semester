# This version contains function definitions
# but the functions have not been implemented
# Analysing marks in Long Jump

# Function for reading the marks of a player:
def read_marks(nameOfPlayer):

    inputMarks=input(F"Input the marks of {nameOfPlayer}:")
    inputList=inputMarks.split()
    marksList=[]
    for i in range(len(inputList)):
        if inputList[i]=="x":
            marksList.append(None)
        else:
            marksList.append(inputList[i])
    return marksList


# Function for calculating the best mark of a player:
def find_best(marks):
    numberList=[]
    for i in range(len(marks)):
        if marks[i]!=None:
            numberList.append(marks[i])
    if len(numberList)==0:
        return None  
    return max(numberList)


# Function for calculating the winner or winners,
# given their best marks:
def determine_winner(nameA, nameB, bestA, bestB):

    """ Assumes 'bestA' and 'bestB' are each either None or an integer.
        Returns a list possibly including each of 'nameA' and 'nameB'
                depending on the best marks between 'bestA' and 'bestB'. """

    if bestA == None:
        if bestB == None:
            winners = []
        else:
            winners = [nameB]
    else:
        if bestB == None:
            winners = [nameA]
        else:
            if bestA > bestB:
                winners = [nameA]
            elif bestA < bestB:
                winners = [nameB]
            else:
                winners = [nameA, nameB]
    
    return winners

# Function for outputting the winner or winners,
# if there are any:
def output_winner_result(namesOfWinners):

    """ Assumes 'namesOfWinners' is a list of strings.
        Returns nothing but prints a result. """

    if len(namesOfWinners) == 0:
        print("Nobody wins.")
    elif len(namesOfWinners) == 1:
        print("Player", namesOfWinners[0], "wins.")
    else:
        print("It is a tie between player", namesOfWinners[0],
                "and player", namesOfWinners[1] + ".")

# Main program:

# Read the marks for both player A and player B:
marksA = read_marks("A")
marksB = read_marks("B")

# Calculate the best mark for both player A and player B:
bestA = find_best(marksA)
bestB = find_best(marksB)

# Calculate the winners and output the result:
winners = determine_winner("A", "B", bestA, bestB)
output_winner_result(winners)
