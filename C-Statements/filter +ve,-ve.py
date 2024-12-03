students_marks = [0,-3,-2,-33,390,-96,100,33,0,-44,77,88,98,-96,45,23,-77,55,88,99,42]
students_marks.sort(reverse=False)

list = []
list2 = []
m=students_marks

for v in m :
    if v>0 and v%2==0:
        print(v,"-is a positive & even number number")
        list.append(v)
    elif v<0 and v % 3==0:
        print(v,"-is a negatve  & 0dd number  ")
        list2.append(v)
    else:
        print(v, "- is not negative and positive")

print(list)
print(list2)