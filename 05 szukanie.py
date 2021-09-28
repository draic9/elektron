# szukanie.py < text.txt
text = input()
out = {}

def Convert(string):
    listitem = list(string.split(" "))
    return listitem

splitList = Convert(text)
alphanumString = {}

for i in range(len(splitList)):
    if splitList[i].isdigit() == True:
        int(splitList[i])
        alphanumString[len(alphanumString)] = splitList[i]
        
print(alphanumString) 