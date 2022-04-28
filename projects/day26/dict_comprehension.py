# Pattern:
# new_dict = [new_key:new_value for item in list]
# new_dict = [new_key:new_value for (key, value) item in dict.items() if test]
import random

""" 
names = ["All", "Bii", "Coo", "Dee"]
person_score = {person: random.randint(0, 10) for person in names}
print(person_score)

students = {"All": 91, "Bii": 64, "Coo": 56, "Dee": 70}
passed_students = {person: score for (person, score) in students.items() if score > 65}
print(passed_students)
"""

import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [15, 75, 99],
}

student_dataframe = pd.DataFrame(student_dict)
# print(student_dataframe)

# for (key, value) in student_dataframe.items():
# print(value)

# Loop through rows of a data frame
for (index, row) in student_dataframe.iterrows():
    print(row.student, row.score)
