List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of mixed Values: ")

print(List)

List= [['Geeks','For'], ['Geeks']]

print("Accessing a element from a Multi-Dimensiobal List")
print(List[0][1])
print(List[1][0])

# Negative Index

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

print("Accessing element using negative indexing")

print(List[-1])

print(List[-3])

# Getting the size of Python list
# Python len() is used to get the length of the list.

List1 = []
print(len(List1))

List2 = [10,20,14]
print(len(List2))

# Taking Input of a Python List

# We can take the input of a list of elements as string, integer, float, etc. But the default one is a string.


#Python programs to take space
# separated input as a string
# split and store it to a list
# and print the string list

string = input("Enter elements (Space-Separated):")

lst = string.split()

print('The list is:', lst)


n = int(input("Enter the size of list :"))
# store integers in a list using map,
# split and strip functions

lst = list(map(int, input("Enter the integer\ elements: ").strip().split()))[:n]

print('The list is:', lst)


