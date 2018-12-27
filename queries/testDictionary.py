#testDictionary.py
choice =input("continue?")
iDict = {}
#another while condition can be used
#while choice.lower() not in {'n','y'}:
while(char != "n" and char !="N"):
	name = input("Name of the field : ")
	dType = input("dataType of the field : ")
	iDict[name] = dType
	print (iDict)
	choice = input("continue? y/n ")
