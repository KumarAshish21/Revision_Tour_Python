# Leftmost Repeating Character
# Efficient 1 

import sys
CHAR = 256
def leftmost(st) :
    findex = [-1] * CHAR
    res = sys.maxsize
    for i in range(len(st)) :
        if (findex[ord(st[i])]==-1) :
            findex[ord(st[i])] = i
        else :
            res = min(res,findex[ord(st[i])])
    if res == sys.maxsize :
        return -1
    else :
        return res
        
st = "abccbd"
print(leftmost(st))


# Leftmost Repeating Character
# Efficient 2

CHAR = 256
def leftmost(st) :
    vis = [False] * CHAR
    res = -1
    for i in range(len(st)-1,-1,-1) :
        if vis[ord(st[i])]==True :
            res = i
        else :
            vis[ord(st[i])] = True
    
    return res
        
st = "abccbd"
print(leftmost(st))

CHAR = 256 
def leftmost(st) :
    count = [0] * CHAR 
    for i in range(len(st)) :
        count[ord(st[i])] += 1 
    for i in range(len(st)) :
        if count[ord(st[i])] > 1 :
            return i 
    return -1 
    
 
st = "abccbd"  
print(leftmost(st))

def leftmost(st) :
    for i in range(len(st)) :
        for j in range(i+1 , len(st)) :
            if st[i] == st[j] :
                return i 
            
    return -1 
    
st = "cabba"
print(leftmost(st))
