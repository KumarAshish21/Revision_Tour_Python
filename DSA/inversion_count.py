def countmerge(self,arr,l,r,mid):
        left=arr[l:mid+1]
        right=arr[mid+1:r+1]
        res,i,j,k=0,0,0,l
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=right[j]
                j+=1
                k+=1
                res+=len(left)-i
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return res
def invcount(self,arr,l,r):
    res=0
    if l<r:
        mid=(l+r)//2
        res+=self.invcount(arr,l,mid)
        res+=self.invcount(arr,mid+1,r)
        res+=self.countmerge(arr,l,r,mid)
    return res
        

def inversionCount(self, arr, n):
    # Your Code Here
    l=0
    r=n-1
    result=self.invcount(arr,l,r)
    return result

