def sqrootfloor(n):
    i=1 
    while(i*i<=n):
        i+=1 
    return i-1

n=9
print(sqrootfloor(n))

def sqrootfloor(n):
    low=1 
    high=n 
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        msq=mid*mid
        if(msq==n):
            return mid
        elif (msq>n):
            high=mid-1
        else:
            low=mid+1 
            ans=mid 
    return ans
    
    
n=9
print(sqrootfloor(n))

# print(1000>4000)
# print(1000*2)
def function(n):
    if n>4000:
        return
    print(n)
    function(n*2)
    print(n)
function(1000)

print(11<=1)

def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return f(n//2)
    return f(n//2) + f(n//2+1)
print(f(11))

def function(n):
    if n==4:
        return n
    else:
        return 2*function (n+1)
print(function (2))

def function (x,y):
    if y==0:
        return 0
    return(x+ function (x,y-1))

def function(x):
    if x==0:
        return
    else:
        print("a")
        return function(x-1)
function (10)

def function(n):
    if n==0:
        return
    print (n%2)
function(n//2)

print(10>0)

def function (n):
    if n>0:
        return (n+function (n-2))
    else:
        return 0
print (function(10))