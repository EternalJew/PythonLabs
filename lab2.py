from random import randint
random_number = randint(1,5)
answer = 0
while random_number != answer:
    print("Choose number of question: \n 1: even number?  \n 2: more / less?")
    number_question = int(input("input number: "))
    if number_question == 1:
        if random_number % 2 == 0:
            print("number even!")
        else:
            print("number not even")

    if number_question == 2:
        if random_number > 3:
            print("number greater than 3")
        elif random_number < 3:
            print("number smallest than 3")
        else:
            print("the number is equal to 3")

    print("type answer: ")
    answer = int(input("input: "))
    if answer == random_number:
        print("right answer")
    else: 
        print("try to choose another answer")
        
        
    

