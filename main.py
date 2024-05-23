# # Task1
# def find_even_nums(num):
#     lst =[]
#     x = list(range(1,num+1))
#     for z in x:
#          if z % 2 == 0:
#              lst.append(z)
#     return lst
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))

# Task2
# def filter_list(ints):
#     lst = []
#     for x in ints:
#         if type(x) == int:
#             lst.append(x)
#     return lst
#
# print(filter_list([1,2,3,"a","b",4]))
# print(filter_list(["A",0,"Edabit",1729,"Python","1729"]))
# print(filter_list(["Nothing","here"]))

# Task3???????????????????????????????????????????????????????????????????????????
# def add_indexes(lst):
#     lst1 = []
#     lst2 =[]
#     for x in lst:
#         lst1.append(lst.index(x))
#         for z in lst1:
#             lst2.append(z+x)
#     return lst2
#
# # print(add_indexes([0,0,0,0,0]))
# print(add_indexes([1,2,3,4,5]))
# print(add_indexes([5,4,3,2,1]))

# Task4?????????????????????????????????????????????????????????????????????????



# Task5
# def next_in_line(lst,num):
#     lst.append(num)
#     for x in lst:
#         lst.pop(0)
#         if lst == []:
#             return '"No list has been selected"'
#         return lst
#
# print(next_in_line([5,6,7,8,9],1))
# print(next_in_line([7,6,3,23,17],10))
# print(next_in_line([1,10,20,42],6))
# print(next_in_line([],6))

# Task6
# def clone(list):
#     list.append(list.copy())
#     return list
#
# print(clone([1,1]))
# print(clone([1,2,3]))
# print(clone(["x","y"]))

# Task7
# def return_only_integer(lst):
#     lst1 = []
#     for x in lst:
#         if type(x) == int:
#             lst1.append(x)
#     return lst1
#
# print(return_only_integer([9,2,"space","car","lion",16]))
# print(return_only_integer(["hello",81,"basketball",123,"fox"]))
# print(return_only_integer([10,"121",56,20,"car",3,"lion"]))
# print(return_only_integer(["String",True,3.3,1]))

# Task8
# def chatroom_status(lst):
#     for x in lst:
#         if len(lst) < 2:
#             return f"{x} is online now!"
#         if len(lst)==2:
#             return f"{lst[0]} and {lst[-1]} are online now!"
#         if len(lst)>2:
#             return f"{lst[0]},{lst[1]} and {len(lst) -2} more online now!"
#     return "No one is online now!"
#
# print(chatroom_status([]))
# print(chatroom_status(["sarahnew"]))
# print(chatroom_status(["mailbox2","sarahnew"]))
# print(chatroom_status(["mailbox2","sarahnew","mindfreeze"]))
# print(chatroom_status(["mailbox2","sarahnew","mindfreeze","openhearted","youngforever"]))

# Task9???????????????????????????????????????????????????????????????????????????
# def list_operation(start,stop,step):
#     lst = []
#     for x in list(range(start,stop,step)):
#         lst.append(x)
#     return lst

# print(list_operation(1,10,3)) +2
# print(list_operation(7,9,2)) +1
# print(list_operation(15,20,7)) +5

# Task10???????????????????????????????????????????????????????????????????????????????????




# Task11????????????????????????????????????????????????????????????????????
def society_name(lst):
    string = ""
    lst1 = []
    for z in lst:
        lst1.append(z[0])
    x = ",".join(sorted(lst1))
    for y in x:
        string+=y
        return string


print(society_name(["Adam","Sarah","Malcolm"]))
print(society_name(["Harry","Newt","Luna","Cho"]))
print(society_name(["Phoebe","Chandler","Rachel","Ross","Monica","Joey"]))

# Task12
# def nums(lst):
#     lst1 = []
#     for x in lst:
#         if x not in lst1:
#             lst1.append(x)
#     return sorted(lst1)
#
# print(nums([1,2,4,3]))
# print(nums([1,4,4,4,4,5,5,7,7,3,3]))
# print(nums([4,6,5,7]))

# Task13
# def setify(lst):
#     lst1 =[]
#     for x in lst:
#         if x not in lst1:
#             lst1.append(x)
#     return sorted(lst1)
#
# print(setify([1,2,3,3]))
# print(setify([4,4,4,4]))
# print(setify([1,5,5,5,3,3,2,2]))

# Task14
# def student_names(dict):
#     lst = []
#     for x in dict:
#         lst.append(dict[x])
#     return sorted(lst)
#
# print(student_names({
#     "Student1" : "Steve",
#     "Student2" : "Becky",
#     "Student3" : "John"
# }))


# Task15
# def greet_people(lst):
#     st = []
#     for x in lst:
#         z = "Hello " + x
#         st.append(z)
#     return st
#
# print(greet_people(["Joe"])),
# print(greet_people(["Angela","Joe"])),
# print(greet_people(["Frank","Angela","Joe"]))

# data = {False,1,2,"name",(1,2,3)}
# for x in data:
#     if type(x) == tuple:
#         print(sum(x))

