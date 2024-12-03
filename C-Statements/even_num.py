students_marks = [0,-3,-2,-33,390,96,100,33,44,77,88,98,96,45,23,77,55,88,99,42]

m=students_marks
m .sort(reverse=False)

for v in m:
    if v%2 == 0:
        print(v,"- is even numbers")
    elif v%3==0:
        print(v,"- is odd number")