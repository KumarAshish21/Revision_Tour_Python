def countFreq(arr, n):
    for i in range(n):
        flag=False
        for j in range(i):
            if(arr[i]==arr[j]):
                flag=True
                break
        if(flag==True):
            continue
        freq=1 
        for j in range(i+1, n):
            if(arr[i]==arr[j]):
                freq=freq+1 
        print(arr[i], freq)
    
    
n=5
arr=[10, 20, 20, 30, 10]
countFreq(arr, n)

def countFreq(arr, n):
    hmp=dict()
    for i in range(n):
        if arr[i] in hmp.keys():
            hmp[arr[i]]+=1 
        else:
            hmp[arr[i]]=1 
    for x in hmp:
        print(x, " ", hmp[x])
    
    
n=5
arr=[10, 20, 20, 30, 10]
countFreq(arr, n)