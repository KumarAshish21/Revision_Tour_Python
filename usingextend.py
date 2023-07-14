# Other than append() and insert() methods, there's one more method for the Addition of elements, extend(),
# this method is used to add multiple elements at the same time at the end of the list.

# append and extend methods can only add elements at the end

# creating a list

List = [1,2,3,4]
print("Initial List: ")
print(List)

# Adding multiple elements using Extend method

List.extend([8, 'Geeks','Always'])
print("\nList after performing Extend Operation: ")
print(List)

# Reversing a List using a reverse method
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)