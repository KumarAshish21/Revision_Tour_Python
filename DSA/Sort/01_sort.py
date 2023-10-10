# sorted()
"""_summary_sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence) either in ascending order or in descending order(does unicode comparison for string char by char) and always returns the a sorted list. This method doesn’t effect the original sequence.
"""
# Syntax: sorted(iteraable, key, reverse=False)
# Parameters: 
# Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted. 
# Key(optional): A function that would serve as a key or a basis of sort comparison. 
# Reverse(optional): If set True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.
# Return Type: Returns a sorted list. 

num =[1,5,6,2,4,3]
sortedNum = sorted(num)
print(sortedNum)

# sort()
"""
sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence. Moreover, sort() is a method of list class and can only be used with lists.
Syntax: List_name.sort(key, reverse=False)
Parameters: 
key: A function that serves as a key for the sort comparison. 
reverse: If true, the list is sorted in descending order.
Return type: None 
"""

num = [6,5,4,3,2,1]
num.sort()
print(num)