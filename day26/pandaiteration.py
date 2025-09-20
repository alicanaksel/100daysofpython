students_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

#Looping through dicts
#for (key,value) in student_dict.items():
#   print(value)

import pandas
student_data_frame= pandas.DataFrame(students_dict)

#loop through a data frame
#for (key,value) in student_data_frame():
    #print(key)#outputs keys of dict
    #print(value) prints whole data in each columns

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
   #print(index) prints 0 1 2
   print(row.student) # or row.score 