student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
keys= list(student_scores.keys())
student_grades={}
for j,i in enumerate(student_scores.values()):
    if i >= 91 and i <= 100:
        i= "Outstanding"
    elif i >= 81 and i <= 90:
        i="Exceeds Expectations"
    elif i>= 71 and i <= 80:
        i="Acceptable"
    else:
        i="Fail"
    student_grades.update({keys[j]:i})

print(student_grades)

    

