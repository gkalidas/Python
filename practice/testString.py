strCheck = "This string is used to check] [if it is working [  or not."

strCheck = strCheck.replace("[","")
strCheck = strCheck.replace("  ","")
strCheck = strCheck.replace("]","")
print(strCheck)
