#Define a function on line 3 called print_grades with one argument, a list called grades_input.
#Inside the function, iterate through grades_input and print each item on its own line.
#After your function, call print_grades with the grades list as the parameter.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for x in grades_input:
    print x
    
print_grades(grades)
