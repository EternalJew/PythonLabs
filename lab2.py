from random import randint
#Task 1
# random_number = randint(1,5)
# answer = 0
# while random_number != answer:
#     print("Choose number of question: \n 1: even number?  \n 2: more / less?")
#     number_question = int(input("input number: "))
#     if number_question == 1:
#         if random_number % 2 == 0:
#             print("number even!")
#         else:
#             print("number not even")

#     if number_question == 2:
#         if random_number > 3:
#             print("number greater than 3")
#         elif random_number < 3:
#             print("number smallest than 3")
#         else:
#             print("the number is equal to 3")

#     print("type answer: ")
#     answer = int(input("input: "))
#     if answer == random_number:
#         print("right answer")
#     else: 
#         print("try to choose another answer")
#Task 2
# rand_a = randint(1,10)
# rand_b = randint(1,10)
# rand_c = randint(1,10)
# print(rand_a , rand_b, rand_c)
# if rand_a + rand_b > rand_c and rand_a + rand_c > rand_b and rand_b + rand_c > rand_a:
#     print("triangle exist")
#     if rand_a == rand_b or rand_b == rand_c or rand_a == rand_c:
#         print("triangle is isosceles")
#     elif rand_a == rand_b == rand_c:
#         print("triangle is equilateral")
#     elif rand_a != rand_b != rand_c:
#         print("triangle is versatile")
# else:
#     print("triangle is not exist")
#Task 4
rand_numb = randint(50,100)
answer_numb = 0
answer_numb = rand_numb
while answer_numb != 1:
    print('-> ',answer_numb, end=' ')
    print(answer_numb)
    if answer_numb == 1:
        print("hypothesis is working!")
    
    if answer_numb % 2 == 0:
        answer_numb = answer_numb // 2
        print(answer_numb)
    else:
        answer_numb = (answer_numb * 3 + 1) // 2
        print(answer_numb, end=' ')
print()