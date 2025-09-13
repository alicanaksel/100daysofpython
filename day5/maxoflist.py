student_scores= [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

max_score=0
for i in range(0,len(student_scores)):
    if i < 14:
        iteration=student_scores[i]
        if iteration > max_score:
            max_score= iteration
       

print(max_score)