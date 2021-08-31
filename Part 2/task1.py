print("TASK 1: multiplication table")
# start the 21s task
# x = int(input("enter x: "))
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in list:
#     z = x * i
#     print(x, '*', i, '=', z)
    
print("TASK 2: Напишіть функцію, яка підносить число до степеня, не використовуючи при цьому вбудовані математичні функції.")
# a = int(input("number: "))
# b = int(input("степінь: "))
# n = 1
# nsave = a
# while n != b:
#     a*= nsave
#     n += 1

# print(a)

print("TASK 3: Напишіть функцію, яка рахує факторіал числа, використовуючи цикли")
# n = int(input("enter: "))
# k = 1
# for i in range(1,n+1):
#     k*=i
# print(k)

print("TASK 4: динамічний масив сортує рядки в порядку зростання")

x=3#rows
y=3#columns
a=[]#create an empty list first
for i in range(x):
    a.append([0]*y)#And again append empty lists to original list
    for j in range(y):
         a[i][j]=int(input("Enter the value: "))

for i in range(x):
    sum_of_rows = sum(a[i])
    print(sum_of_rows)
        

         
for i in range(x):
    for j in range(y):
        print(a[i][j], end = ' ')
    print("\n")

