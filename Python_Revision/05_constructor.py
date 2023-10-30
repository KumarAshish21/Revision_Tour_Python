# mistake 
# naming python files with built-in names

# import pickle

# print(pickle.dumps("Hello World"))

# # mistake over-riding imported contents
# from math import sqrt

# sqrt = sqrt(25)
# print(sqrt)
# print(sqrt(49))

# Problem of default arguments

# students = ['Ashish','Chaurasiya']

# def add_students(name,students=[]):
#     students.append(name)
#     print(students)
    
# add_students("Ashish")
# # add_students("Chaurasiya")

# import time

# from datetime import datetime

# def display_time(time = datetime.now()):
#     print(time)
    
# display_time()
# time.sleep(10)
# display_time()

# Mistake 4-> mistake while using higher order functions

# data = [89,90,56,67,82,87]
# def logic(ele):
#     if ele%2==0:
#         return True
    
    
# filtered_object= filter(logic,data)

# # print(list(filtered_object))

# for ele in filtered_object:
#     print(ele)

# by converting into list
# for loop
# Genrators is exhaust only one time used iterator
# Genrator is used for more efficiency and performance inhance

# mistake 5 mistake while copying data

# import copy

# data = [10,20,[1,2,3]]

# copied_data = copy.copy(data)

# print(copied_data)

# copied_data[2][1] = "Ashish"
# print(copied_data)
# print("original:",data)

