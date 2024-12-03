students_marks = [90,96,100,33,44,77,88,98,96,45,23,77,55,88,99,42]
students_marks .sort(reverse=True)
grade_A=[]
grade_B=[]
grade_C=[]

for v in students_marks:
    if v<35 :
        print(v,"- failed in exam")
    elif v>=35 and v<=65:
        print(v,"- c Grade good")
    elif v>65 and v<=85:
        print(v,"- B Grade super")
    elif v>85:
        print(v,"-A Grade Excellent")

students_marks1 = [90,96,100,33,44,77,88,98,96,45,23,77,55,88,99,42]

for v in students_marks1:
    if v < 35 :
        grade_C.append(v)
    elif v>35 and v<=65:
        grade_B.append(v)
    elif v>65 :
        grade_A.append(v)

print(grade_A)
print(grade_B)
print(grade_C)


