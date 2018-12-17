#for each student in your students list, print out that student's data, as follows:
#print the student's name
#print the student's homework
#print the student's quizzes
#print the student's tests

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
students = [lloyd,alice,tyler]
for s in student:
  print s["name"]
  print s["homework"]
  print s["quizzes"]
  print s["tests"]
    
