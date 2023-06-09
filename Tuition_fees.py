# Practice problem - Tuition fees
# Let's solve this practice problem.

# You will attend tuitions for 
# �
# X weeks, and the cost of tuition per week is 
# �
# Y dollars.
# You need to compute and output your total tuition fees.
t = int(input())
for i in range(t): 
    X, Y = map(int, input().split())
    S = X * Y
    print(S)