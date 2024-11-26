import random

names = ["Alex", "Beth", 'Caroline', 'Dave', 'Eleanor','Freddie']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score > 65}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)