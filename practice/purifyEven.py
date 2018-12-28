#purifies even numbers and returns them from a given list

def purify(l):
  print l
  n = []
  for x in l:
    print x
    if x%2==0:
      n.append(x)
  return n
