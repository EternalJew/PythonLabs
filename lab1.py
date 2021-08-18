from array import *
import math
#Task 1
surname = input("Enter your surname:")
name = input("Enter your name: ")
fName = input("Enter your father name:")
print("/ " + surname + "/ " + name + "/ " + fName)
#Task 2
arr = array('i', [8,1,7,4])
print(arr[0] > arr[2] and arr[0] > arr[0] / arr[3] == 2)    
#Task 3
print("Введіть коефіцієнти")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискримінант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Коренів немає")