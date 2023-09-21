nameList=[]
heightList=[]
highestPlayersDict={}
for i in range(3):
    currPlayerName=input("Type the players name: ")
    currPlayerHeight=int(input("Type the players name: "))
    nameList.append(currPlayerName)
    heightList.append(currPlayerHeight)
highestPlayerHeight=max(heightList)
for i in range(len(heightList)):
    if heightList[i]==highestPlayerHeight:
        highestPlayersDict[nameList[i]]=highestPlayerHeight
for kvp in highestPlayersDict:
    print(f"The tallest player is {kvp} with a height of {highestPlayersDict[kvp]}")
