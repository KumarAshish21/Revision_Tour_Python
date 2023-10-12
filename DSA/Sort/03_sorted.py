# Syntax: sorted(iterable, key, reverse)

 
# Parameters: sorted takes three parameters from which two are optional. 

# Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
# Key(optional): A function that would serve as a key or a basis of sort comparison.
# Reverse(optional): If True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.
# Return: Returns a list with elements in sorted order.

l = [10, 20, 14]
ls = sorted(l)
print(l)
print(ls)


l = [10, -15, -2, 1]
ls = sorted(l, key=abs, reverse= True)
print(ls)

l = (10,15,20,54,2)
ls = sorted(l)
print(ls)
a = ("ashish","shubham","Viany")

print(sorted(a))

d = {1:'ashish',2:'Vinay', 3 :'Atul', 4: 'Ajay', 5: 'Ayan'}

print(sorted(d.values()))

# Stability in Sorting Algorithm
# A Sorting algorithm is said to be stable if two objects with the equal keys appear in the same order in sorted output as they appear in the input data set.
l = [("Ashish", 25),("Ajay",26),("Atul",24)]
l.sort()
print(l)

# Which sorting algorithms are stable? 
# Some Sorting Algorithms are stable by nature, such as Bubble Sort, Insertion Sort, Merge Sort, Count Sort, etc.

# Which sorting algorithms are unstable? 
# Quick Sort, Heap Sort etc., can be made stable by also taking the position of the elements into consideration


