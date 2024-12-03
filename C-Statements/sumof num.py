l1 = [2,66, 5, 7, 8]

total_sum = sum(l1)


print("Sum of elements:", total_sum)
if total_sum % 2 == 0:
    print("The sum is even.")
else:
    print("The sum is odd.")


num_to_check=88
if num_to_check in l1:

    print("the num is available",num_to_check)
else:
    print("the",num_to_check,"number is not available" )


list5 = [2,4,3,4,6,7,99,22,55,100]
num1 = 0
num2 = 0
for I in list5:
      if I>num1:
             num2=num1
             num1=I
      elif I>num2 and I!=num1:
             num2=I
print(num2)


age =2

if age >= 18:
    print("adilt")

    if age >=65:
        print("sc")
    else:
        print("mid level")
else:
    if age >= 13:
        print("teenager")
    else:
        print("child")

age = 2

if age >= 18:
    print("Adult")
    if age >= 65:
        print("Senior Citizen")
    else:
        print("Young Adult")
else:
    if age >= 13:
        print("Teenager")
    else:
        print("Child")
