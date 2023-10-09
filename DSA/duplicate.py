# # Remove Duplicates from Sorted Array
# def remeDuplicate(nums):
#     res = []
#     for i in range(len(nums)):
#         if nums[i] not in res:
#             res.append(nums[i])
#     return res
# nums = [1,1,2]
# # print(remeDuplicate(nums))

# # def removeDuplicates(nums):
# #     unique_set = set()
# #     i = 0
# #     while i < len(nums):
# #         if nums[i] not in unique_set:
# #             unique_set.add(nums[i])
# #             i+=1
            
# #         else:
# #             nums.pop(i)
# #     return len(nums)

# def removeDuplicatesArray(nums):
#     slow = []
#     for i in range(len(nums)):
#         if nums[i]!= nums[slow]:
#             slow +=1
#         nums[slow] = nums[i]
#     return slow + 1

# print(removeDuplicatesArray(nums = [1,1,2]))

# def removeDuplicates(nums):
#     if not nums:
#         return 0

#     unique_count = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[unique_count] = nums[i]
#             unique_count += 1

#     return unique_count



def removeDuplicates(nums):
    if not nums:
        return 0

    unique_nums = [nums[0]] + [nums[i] for i in range(1, len(nums)) if nums[i] != nums[i - 1]]
    
    return len(unique_nums)
nums = [1,1,2]
print(removeDuplicates(nums))