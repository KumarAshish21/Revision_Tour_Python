# Task
# Write a program which does the following

# Accepts the count of test cases - 
# �
# t
# Each test case has one integer 
# �
# N

t = int(input())
for i in range(t):
    #Accept 1 integer as input.
    N = int(input())            
    #1st condition in the problem
    if N<=100:              
        print('Good')
    #2nd condition in the problem
    elif N>=100 and N<=200: 
        print('Better')
    #3rd condition in the problem
    else:                   
        print('Best')