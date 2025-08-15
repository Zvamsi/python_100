student_marks = {
    "Rahul": 85,
    "Priya": 72,
    "Amit": 93,
    "Neha": 58,
    "Sohan": 41,
    "Kavita": 67,
    "Vikram": 79,
    "Anjali": 88,
    "Rohit": 35,
    "Divya": 96
}
student_grades={}

for student in student_marks:
    if student_marks[student] >80:
        grade='Distinction'
    elif student_marks[student]>60:
        grade='First Class'
    elif student_marks[student]>40:
        grade='Pass'
    else:
        grade='Fail'
    student_grades[student]=grade

print(student_grades)

