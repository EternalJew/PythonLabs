import math 
#Task 2
number_of_vertecs = int(input("Input number of vertecs: "))

def triangle():
    a1 = float(input("Input A1: "))
    a2 = float(input("Input A2: "))
    b1 = float(input("Input B1: "))
    b2 = float(input("Input B2: "))
    c1 = float(input("Input C1: "))
    c2 = float(input("Input C2: "))
    a = math.sqrt(a1**2 + a2**2)
    b = math.sqrt(b1**2 + b2**2)
    c = math.sqrt(c1**2 + c2**2)
    p = (a + b + c) / 2.0
    s = math.sqrt((p*(p - a) * (p - b) * (p - c)))
    print(p*2)
    print(s)

def polygon():
    a1 = float(input("Input A1:"))
    a2 = float(input("Input A2:"))
    number_of_sides = number_of_vertecs
    a = math.sqrt(a1**2 + a2**2)
    b = 3.14 / number_of_sides
    s = 0.25 * number_of_sides * a**2 * (math.cos(b) / math.sin(b))
    p = a * number_of_sides
    print(p)
    print(s)
    

if number_of_vertecs == 3:
    triangle()
elif number_of_vertecs > 4:
    polygon()
#Task 3

    
    
    
    