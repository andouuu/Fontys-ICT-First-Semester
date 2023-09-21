word=input("Type a word: ")
letterList=[]
for each in word:
    letterList.append(each)
print(letterList)
letter=input("Type a letter: ")
if letter in letterList:
    print("Yes")
else: 
    print("No")

for i in range(len(letterList)):
    letterList[i]='*'        
print(letterList)
