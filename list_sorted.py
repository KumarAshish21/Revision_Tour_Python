# using loop
def list_sorted(l):
    i = 1
    while i < len(l):
          if l[i] < l[i-1]:
               return False
          i = i+1
    return True
l = [10,20,30,15,40]
if list_sorted(l):
    print("Yes")
else:
    print("No")


# using sorted function
# what is the difference between sort and sorted?

#  when you call sort function it's modifai list using sort function 
# sorted function, it will not be modifai list it is create a new list which is the sorted given list.

def isSorted(l):
    sl = sorted(l)
    if sl ==l:
        return True
    else:
        return False
l = [10,20,5,30]
if isSorted(l):
    print('Yes')
else:
    print("No")     