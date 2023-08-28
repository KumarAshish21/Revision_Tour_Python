def fun(n):
    if n==0:
        return
    fun(n/2)
    print(n%2)
print(fun(13))