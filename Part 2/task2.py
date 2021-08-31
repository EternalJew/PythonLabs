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
    

    