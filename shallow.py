mylist = [[1,2,3],[4,5,6],[7,8,'a']]
print("id of mylist:",id(mylist))
print("id of first element:",id(mylist[0]))
print("id of second element:",id(mylist[1]))
print("id of third element:",id(mylist[2]))

newlist = mylist
print("-"*50)
print("id of newlist:",id(newlist))
print("id of first element:",id(newlist[0]))
print("id of second element:",id(newlist[1]))
print("id of second element:",id(newlist[2]))

newlist[1][2] =6000
print(newlist)

# sometimes you may want to have the original
# values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:
# 1) Deep Copy
# 2) Shallow Copy
# - To make these copy work, we use the copy module

# shallow copy
import copy

shallow_list = [[1,2,3],[4,5],[6,'a']]
new_list = copy.copy(shallow_list)
print(new_list)
# new_list[2][2] ="hello"
# print(new_list)


# deep copy



