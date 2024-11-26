import random

names = ["Alex", "Beth", 'Caroline', 'Dave', 'Eleanor','Freddie']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score > 65}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:temp_c * 9/5+ 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

import pandas

student_data_frame = pandas.DataFrame(student_dict)