import math
class Fraction:
    a = 1
    b = 5
    
    def check_correct_fraction(self):
        c = self.a / self.b
        if c < 1:
            print("fraction is correct")
        else:
            print("fraction is not correct")
            
link = Fraction()
link.check_correct_fraction()

class Vector:
    #static vector
    x = 1
    y = 2
    print("Vector A: ", x, y )

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
    
    def Vector_addition(self):
        print("addition: ")
        print("Vector B: ", self.coord_x + Vector.x, self.coord_y + Vector.y)
    
    def Vector_subtraction(self):
        print("subtraction: ")
        print("Vector B: ", self.coord_x - Vector.x, self.coord_y - Vector.y)
        
vector_B = Vector(3, 4)
# x = int(input("Choose +/- : "))
x = 1
if x == 1:
    vector_B.Vector_addition()
elif x == 2:
    vector_B.Vector_subtraction()
    
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
        
    def smallest(self, category):
        self.category = category
        
class Turtle(Animal):
    category = "reptile"  

class Snake(Animal):
    category = "reptile"

class Lion(Animal):
    category = "hunter"
    
class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
        
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle")
snake = Snake("Snake")
lion = Lion("Lion")

zoo.add_animal(turtle)
zoo.add_animal(snake)
zoo.add_animal(lion)
print("--------------------")
print(zoo.total_of_category("reptile"))
print(zoo.total_of_category("hunter"))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Segment:
    
    point_A = Point(1,2)
    point_B = Point(3,2)
    
    def length_segment(self):
        segment_AB = math.sqrt((self.point_B.x - self.point_A.x)**2 + (self.point_B.y - self.point_A.y)**2)
        print ("AB = ", segment_AB)
        

link = Segment()
link.length_segment()
    
class Triangle():
    
    point_A = Point(1,2)
    point_B = Point(3,2)
    point_C = Point(2,4)
    def perimetr(self):
        segment_AB = math.sqrt((self.point_B.x - self.point_A.x)**2 + (self.point_B.y - self.point_A.y)**2)
        segment_AC = math.sqrt((self.point_C.x - self.point_A.x)**2 + (self.point_C.y - self.point_A.y)**2)
        segment_BC = math.sqrt((self.point_C.x - self.point_B.x)**2 + (self.point_C.y - self.point_B.y)**2)
        P = segment_AB + segment_BC + segment_AC
        print ("P = ", P)

link = Triangle()
link.perimetr()
    
class Human:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Change_name_method(self):
        print( self.name)
        self.name.clear()
        self.name = input("enter new name: ")
        print("New name: ", self.name)
        
# l = Human(['ToM'], 18)
# l.Change_name_method()
class Student(Human):
    def __init__(self, institute, marks_list):
        self.institute = institute
        self.marks_list = marks_list
        
    def add_new_mark(self, new_mark):
        print(self.marks_list)
        self.marks_list.append(new_mark)
        print(self.marks_list)
        self.marks_list.sort()
        print(self.marks_list)
    
    def avarage_mark(self):
        
        def __len__(self):
            return len(self.marks_list)
        
        avar_mark = sum(self.marks_list) / len(self.marks_list)
        
        print("Середній бал: ",avar_mark)
        
# list_of_marks = Student('nuwm', [1,2,3,5])
# list_of_marks.avarage_mark()
#
# add_mark_to_list = Student('nuwm', [1,2,3,5])
# add_mark_to_list.add_new_mark(4)

        
        