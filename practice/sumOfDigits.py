
#This is my solution
def digit_sum(n):
  total = 0
  digit_str = str(n)
  for char in digit_str:
    total +=char
  print total
  return total
digit_sum(3456)


#Alternate Solution:
#This is given by codecademy
#def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total
  
print digit_sum(1234)
