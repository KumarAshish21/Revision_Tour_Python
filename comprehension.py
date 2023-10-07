
# It is a way of writing compact code in python.
# Syntax-01:- Normal[expression for variable in iterable]
# Syntax-02: - If condition [expression for variable in iterable if cond]
# Syntax-03: - Nested if's[expression for variable in iterable if condi if cond21
# Syntax-04:- If else [expression if cond else expression for variable in iterable]
# Syntax-01
nums = [3,6,8,12,14,15]
ab = []
for i in nums:
    if i%2==0:
        if i%3==0:
            ab.append(i*i)
print(ab)



print([num*num for num in nums if num%2==0 if num%3==0])

# Syntax-04:- If else [expression if cond else expression for variable in iterable]
nums = [3,6,8,12,14,15]
result = []
for num in nums:
    if num%2 ==0:
        result.append(num*num)
    else:
        result.append(num*num*num)
print(result)

print([num*num if num%2==0 else num*num*num for num in nums])

#syntax-05: - [expression if cond else expression for var in iterable]
lst = []
for i in range(3,6):
    for j in range(5,7):
        lst.append(i*j)
print(lst)

print([i*j for i in range(3,6) for j in range(5,7)])

# note Compact and elegent code
# less code
# Faster execution
# Difficult understand

        
nums = [90,-8,32,43,20]
status = []
if num>0:
    status.append(num)
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("Postive" if num>0 else "Negative" if num<0 else "Zero")

# List comprehension

print(["Postive" if num>0 else "Negative" if num<0 else "Zero" for num in nums])

checkup_fees = []
ages = [23,78,16,43,21,17,12,48]

for age in ages:
    if age < 18:
        checkup_fees.append(100.00)
    elif age < 30 and age >= 18:
        checkup_fees.append(500.00)
    elif age <45 and age >= 30:
        checkup_fees.append(700.00)
    else:
        checkup_fees.append(200.00)
print(checkup_fees)

print([100.00 if age<18 else 500.00 if age < 30 and age >= 18 else 700.00 if age <45 and age >=31 else 200.00 for age in ages])


# 

A = 10
def demo():
    global A
    A = A + 5
    print(A)
demo()
print(A)