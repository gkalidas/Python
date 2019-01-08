#On line 3, define a function, grades_sum, that does the following:
#Takes in a list of scores, scores
#Computes the sum of the scores
#Returns the computed sum.
#Call the newly created grades_sum function with the list of grades and print the result.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for x in scores:
    total += x
  return total
    
print grades_sum(grades)
