
'''
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''

studentsName=["Ravi","Ammu","Teja","Akash","Harshitha"]
cs_marks=[56,67,45,89,50]
math_marks=[78,94,76,38,86]
eng_marks=[98,87,85,92,90]

pass_marks=50

# function for evalutaing the grade

def calculate(mark):
    if mark>50:
        if mark>90:
            return 'A'
        elif mark > 80 and mark<90:
            return 'B'
        else:
            return 'Pass'
    else:
        return 'Fail'
        

for i in range(len(studentsName)):
    grade_cs=calculate(cs_marks[i])
    grade_math=calculate(math_marks[i])
    grade_eng=calculate(eng_marks[i])
    
    if (grade_cs=='A' and grade_math=='A' and grade_eng=='A') or (grade_cs=='A' and grade_math=='B' and grade_eng=='B') or (grade_cs=='B' and grade_math=='A' and grade_eng=='B') or (grade_cs=='B' and grade_math=='B' and grade_eng=='A'):
        print(f'{studentsName[i]} got A in all subjects or atleast one A and the rest B')