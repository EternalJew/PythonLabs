# print("Task 1")
# firstVariable = input('Enter your firstVariable:')
# secondVariable = input('Enter your secondVariable:')
# try:
#     fV = int(firstVariable)
#     sV = int(secondVariable)
#     print(fV / sV)
# except:
#     print('The variable is not a number')

# try:
#     fV = str(firstVariable)
#     sV = str(secondVariable)
#     print(fV + sV)
# except:
#     print('The variables is not a string')
    
# try:
#     fV = str(firstVariable)
#     sV = int(secondVariable)
#     print(fV * sV)
# except:
#     print('The variables is not a string and int')

print("Task 2")

my_file = open("/home/user/git/PythonLabs/filesLab7/text.txt", "w+")
my_file.write("si!")
my_file.close()
my_file_1 = open("/home/user/git/PythonLabs/filesLab7/exp.zip", "w")
my_file_1.close()