list = [1, 2, 3, 4, 5]
# for i in a[::-1]:
#     print(list)
# gen_obj = (x for x in list[::-1])
# for val in gen_obj:
#     print(val)
t = input("1: del all elem of list, 2: input element in list, 3: del elem in start, end, random place in list")

if t == '1':
    list[:] = []
    print(list)

elif t == '2':
    elem = int(input("input elem which you want to add: "))
    index = int(input("input index of list: "))
    list.insert(index, elem)
    print(list)

elif t == '3':
    index = int(input("input index of list: "))
    list.pop()
    list.pop(0)
    list.pop(index)
    print (list)
    
