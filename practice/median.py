#returns median from given list

def median(l):
  #l = [5,4,7,3,8]
  ll=len(l)/2
  print "ll : %s"%ll
  l=sorted(l)
  if (len(l))%2==0:
    med = (l[ll] + l[ll-1])/float(2)
    print "Even %s"%l
    print med
  else:
    med = l[ll]
    print "odd %s"%l
    print med
    
  return med
