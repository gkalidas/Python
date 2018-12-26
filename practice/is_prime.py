#This is mine one
def is_prime(x):
  n = 2
  count=0
  while x-1 > 0:
    if(n%x==0):
      count +1
      if(count>0):
        print "Not a prime number"
        return False
      else:
        print "prime number"
        return True
        

#this is good one
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print is_prime(13)
print is_prime(10)
