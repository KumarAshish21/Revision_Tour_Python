nums =  [1,2,3,4,5]

mydict = {}

for num in nums:
    if num%2 ==0:
        mydict[num] = num**2
print(mydict)


print({num:num**2 for num in nums if num%2==0})

str1 = "coding"
mydict = {}
for char in str1:
    mydict[char.upper()] =(ord(char),ord(char.swapcase()))
print(mydict)

print({char.upper():(ord(char),ord(char.swapcase()))for char in str1})


