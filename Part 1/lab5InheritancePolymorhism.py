class Avto:
    def carAvto(self):
        print(engine, kuzov)

engine = "3.0tdi"
kuzov = "sedan"
auto = Avto()
Avto.carAvto(auto)

class Dacia:
    def carDacia(self):
        print(nameDacia, countDacia)

nameDacia = "Dacia"
countDacia = 1000

dacia = Dacia()
Dacia.carDacia(dacia)

class Audi:
    def carAudi(self):
        print(nameAudi, countAudi)
        
nameAudi = "Audi"
countAudi = 1001

audi = Audi()
Audi.carAudi(audi)

class Avtodacia(Avto, Dacia):
    pass
carDacia = Avtodacia()
print("--------------------")
Avtodacia.carAvto(carDacia)
Avtodacia.carDacia(carDacia)

class Avtoaudi(Avto, Audi):
    pass
carAudi = Avtoaudi()
print("--------------------")
Avtoaudi.carAvto(carAudi)
Avtoaudi.carAudi(carAudi)

print("Task 2")

class Editor:
    def view_documents(self):
        print("Doc reading.....")
    
    def edit_documents(self):
        print("reading is not available for free version((")
        
output = Editor()
Editor.view_documents(output)
Editor.edit_documents(output)
print("---------------------------")

class ProEditor(Editor):
    def edit_documents(self):
        print("you can edit this doc")
        
key = str(input("Enter key: "))
if key == "1":
    login = ProEditor()
    ProEditor.edit_documents(login)
else:
    login_incorrect = Editor()
    Editor.edit_documents(login_incorrect)
    

print("Task 3")
class Auto:
    def ride(self):
        print("riding on a ground")
        
class Plane:
    def fly(self):
        print("fly in the sky")
        
class AutoPlane(Auto, Plane):
    pass

a = AutoPlane()
a.ride()
a.fly()
    

        
    
    
