from random import randint

rand_list = [randint(1, 10) for i in range(5)]
    
print("Task 1")

def CheckMultiplicity(A):
    if A == []:
        return 0
    else:
        count = CheckMultiplicity(A[1:])
        neg = []
        if A[0] % 3 == 0:
            neg.append(A[0])
            count = count + 1
            print(neg)
        
        return count

n = CheckMultiplicity(rand_list)
print(n)



print("Task 2")

def CalcSumOfNumbers(A):
    if A == []:
        return 0
    else:
        summ = CalcSumOfNumbers(A[1:])
        
        summ = summ + A[0]
        
        return summ
    
List = [1, 2 ,3 ,4]

summ = CalcSumOfNumbers(List)

print(summ)   

print("Task 4")

def PrintNegativeNumbers(A):
    if A == []:
        return 0
    else:
        count = PrintNegativeNumbers(A[1:])
        neg = []
        if A[0] < 0:
            neg.append(A[0])
            count = count + 1
            print(neg)
        
        return count

list = [-2, 3, 8, -11, -4, 6 ]

n = PrintNegativeNumbers(list)
print(n)



        