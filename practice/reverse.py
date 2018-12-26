#program to reverse the string

def reverse(text):
  a=[]
  b = len(text)
  while b >0:
    b -= 1
    a.append(text[b])
    print text[b]
    c=a
    
  return c
  
#working one
def reverse(text):
  print text
  a=""
  l = len(text)
  for x in range(l-1,-1,-1):
    #print l
    a += text[x]
    #print a
  print
  print a
  return a

reverse("hsenaG")
