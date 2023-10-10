def rotate(nums,k):
    L = len(nums)
    if L == k: return
    k = k%L
    nums.reverse()
    for i in range(k//2):
        nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
    for i in range(k, (L+k)//2):
        nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums,k))