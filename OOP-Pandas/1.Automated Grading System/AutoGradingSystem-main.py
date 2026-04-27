#1
class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.maths = math_score
        self.sciences = science_score
        self.status = ''
    def check_status(self):
        average = (self.maths + self.sciences) / 2
        if average >= 50:
            self.status = 'Pass'
        else:
            self.status = 'Fail'
#2
import pandas as pd
df = pd.read_csv('raw_grades.csv')
df = df.fillna(0)
df.to_csv('raw_grades.csv', index=False)
#3
studentObject = []
for index, row in df.iterrows():
    s = Student(name = row['Student_Name'], math_score = row['Math_Score'], science_score = row['Science_Score'])
    studentObject.append(s)
    s.check_status()
#4
final_record = []
for s in studentObject:
    final_record.append({
        'Student_Name': s.name,
        'Math_Score': s.maths,
        'Science_Score': s.sciences,
        'Status': s.status
    })
df_final = pd.DataFrame(final_record)
df_final["School Year"] = "2023-2024"
df_final.to_csv('final_grades.csv', index=False)
