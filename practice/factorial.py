#factorial
#I added "b" in this program and still their(codecademy's) compiler telling me that it's not correct.

def factorial(x):
  fac = 1
  b = int(x)
  while b>0:
    fac *= b
    b -= 1
  return fac
  
  
#codecademy's solution
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print factorial(5)
