# pop() function can also be used to remove and return an elements from the list, but by default it removes only the last element of the list, to remove an element from a specific position of the list, the index of the element is passed as an arguments to the pop() methods.

List=[1, 2, 3, 4, 5]

# Removing element from the set using the pop() method

List.pop()
print("\nList after popping an element: ")

print(List)

List.pop(2)

print("\nList after popping a specific element: ")
print(List)