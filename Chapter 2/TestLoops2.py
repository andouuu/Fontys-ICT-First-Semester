word=input("Type your word: ")
letters=list(word)
newList=[
    letter 
         if letter=="e" 
         else "*" 
            for letter in letters]
for i in range(0,len(letters),1):
    if letters[i]!='e':
        letters[i]='*'
print("".join(newList))
