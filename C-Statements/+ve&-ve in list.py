students_mark1 = [0,-3,-2,-33,390,-96,100,33,-44,77,88,98,-96,45,23,-77,55,88,99,42]
students_mark1.sort(reverse=False)
positive_list = []
negative_list = []
for v in students_mark1:
      if v>0 :
          print(v,"is positive")
          positive_list.append(v)
      elif v<0 :
          print(v,"is a negative")
          negative_list.append(v)
print(positive_list)
print(negative_list)