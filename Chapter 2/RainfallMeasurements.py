import math;
def averageNum(numbers):
    if len(numbers)==0:
        return "You didnt add any numbers!!!"
    return sum(numbers)/len(numbers)

def inputList(rainfall):
    inputNum=input("Current number to add: ")
    while inputNum!="":
        rainfall.append(float(inputNum))
        inputNum=input("Current number to add: ")
    
def averageSegment(numbers,start,end):
    thisWeekList=[]
    for i in range(start,end):
        thisWeekList.append(numbers[i])
    return averageNum(thisWeekList)

def output(numbers,weekNumbers,monthNumbers):
    outputString="The total average is "
    outputString+=F"{averageNum(numbers)}"
    if len(weekNumbers)!=0:
        for i in range(len(weekNumbers)):
            outputString+=F", week {i+1} average is {weekNumbers[i]}"
    if len(monthNumbers)!=0:
        for i in range(len(monthNumbers)):
            outputString+=F", month {i+1} average is {monthNumbers[i]}"
    print(outputString)
    
def main():
    
    rainfall=[]
    inputList(rainfall)
    weekCount=0
    monthCount=0
    weeksAverages=[]
    monthsAverages=[]
    for i in range(math.floor(len(rainfall)/7)):
        weeksAverages.append(averageSegment(rainfall,weekCount*7,weekCount*7+7))
        weekCount+=1
    for i in range(math.floor(len(rainfall)/30)):
        monthsAverages.append(averageSegment(rainfall,monthCount*30,monthCount*30+30))
        monthCount+=1
    output(rainfall,weeksAverages,monthsAverages)

main()