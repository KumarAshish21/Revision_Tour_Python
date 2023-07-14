# creating list
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements

List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# # Adding elements to the List
# # using Iterator
for i in range(1,4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List

List.append((5, 6))

print("\nList after Addition of a Tuples: ")
print(List)

# # Addition of List to a List
List2 = ['For', 'Geeks']

List.append(List2)
print("\nList after Addition of a List: ")
print(List)