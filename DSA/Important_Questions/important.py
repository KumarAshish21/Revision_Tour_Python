"""
Array

Two Sum
Best Time to Buy and Sell Stock
Contains Duplicate
Product of Array Except Self
Maximum Subarray
Maximum Product Subarray
Find Minimum in Rotated Sorted Array
Search in Rotated Sorted Array
3 Sum
Container With Most Water

Binary

Sum of Two Integers
Number of 1 Bits
Counting Bits
Missing Number
Reverse Bits

Dynamic Programming

Climbing Stairs
Coin Change
Longest Increasing Subsequence
Longest Common Subsequence
Word Break Problem
Combination Sum
House Robber
House Robber II
Decode Ways
Unique Paths
Jump Game

Graph

Clone Graph
Course Schedule
Pacific Atlantic Water Flow
Number of Islands
Longest Consecutive Sequence
Alien Dictionary (Leetcode Premium)
Graph Valid Tree (Leetcode Premium)
Number of Connected Components in an Undirected Graph (Leetcode Premium)

Interval

Insert Interval
Merge Intervals
Non-overlapping Intervals
Meeting Rooms (Leetcode Premium)
Meeting Rooms II (Leetcode Premium)

Linked List

Reverse a Linked List
Detect Cycle in a Linked List
Merge Two Sorted Lists
Merge K Sorted Lists
Remove Nth Node From End Of List
Reorder List

Matrix

Set Matrix Zeroes
Spiral Matrix
Rotate Image
Word Search

String

Longest Substring Without Repeating Characters
Longest Repeating Character Replacement
Minimum Window Substring
Valid Anagram
Group Anagrams
Valid Parentheses
Valid Palindrome
Longest Palindromic Substring
Palindromic Substrings
Encode and Decode Strings (Leetcode Premium)

Tree


Maximum Depth of Binary Tree
Same Tree
Invert/Flip Binary Tree
Binary Tree Maximum Path Sum
Binary Tree Level Order Traversal
Serialize and Deserialize Binary Tree
Subtree of Another Tree
Construct Binary Tree from Preorder and Inorder Traversal
Validate Binary Search Tree
Kth Smallest Element in a BST
Lowest Common Ancestor of BST
Implement Trie (Prefix Tree)
Add and Search Word
Word Search II

Heap

Merge K Sorted Lists
Top K Frequent Elements
Find Median from Data Stream

"""

#
# Find All People With Secret
# You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
#
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
#
# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
#
# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
# Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
# Output: [0,1,2,3,5]

# Number of days:
#
# days = int(input("Number of days :"))
# for n in range(days + 1):
#     sum = n * (n+1)//2
# print(sum)
#
# # count of numbers
# x = 92
# count = 0
# while x > 0:
#     x = x //10
#     count += 1
#
# print(count)
#
# # Number is plindrome or not
#
# n = int(input("Enter the number: "))
# temp = n
# rev = 0
# while (n > 0):
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n // 10
# if temp == rev:
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")
#
# # Factorial of a number
#
# n = int(input("Enter the number :"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"Factorial is {fact}")
#
# n = int(input("Enter the number :"))
# fact = 1
# while n > 0:
#     fact = fact * n
#     n -= 1
# print(f"Factorial is {fact}")
#
# # Prime Number
#
# n = int(input("Enter the number :"))
# if n > 1:
#     for i in range(2,n):
#         if n % i ==0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")
#
# # Fibonacci Series
# n = int(input("Enter the number :"))
# a = 0
# b = 1
# print(a)
# print(b)
# c = 0
# for i in range(2,n):
#     c = a + b
#     a = b
#     b = c
#     print(c)
#
# # Armstrong Number
# n = int(input("Enter the number :"))
# temp = n
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit ** 3
#     n = n // 10
# if temp == sum:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
#
# # Remove duplicate from list
# list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# list1 = []
# for i in list:
#     if i not in list1:
#         list1.append(i)
# print(list1)
#
# # Reverse a string
# string = "Hello World"
# print(string[::-1])
#
# # Method 2 Reverse string
# string = "Hello World"
# rev = ""
# for i in string:
#     rev = i + rev
# print(rev)
#
# # Remove duplicate from string
# string = "Hello World"
# list1 = []
# for i in string:
#     if i not in list1:
#         list1.append(i)
# print("".join(list1))
#
# # Count the number of words in a string
# string = "Hello World"
# print(len(string.split()))
#
# # Count the number of words in a string
# string = "Hello World"
# count = 0
# for i in string:
#     if i == " ":
#         count += 1
# print(count)
#
# # Maximum and Minimum in Array
#
# list = [1,2,3,4,5,6,7,8,9]
# print(max(list))
# print(min(list))
#
# # Method 2
# list = [1,2,3,4,5,6,7,8,9]
# max = list[0]
# min = list[0]
# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max)
# print(min)
#
# # Sum of all elements in array
# list = [1,2,3,4,5,6,7,8,9]
# print(sum(list))
#
# # Method 2
# list = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in list:
#     sum += i
# print(sum)
#
# # Reverse an array
# list = [1,2,3,4,5,6,7,8,9]
# print(list[::-1])
#
# # Method 2
# list = [1,2,3,4,5,6,7,8,9]
# list1 = []
# for i in list:
#     list1.insert(0,i)
# print(list1)
#
# # Method 3
# list = [1,2,3,4,5,6,7,8,9]
# list1 = []
# for i in range(len(list)-1,-1,-1):
#     list1.append(list[i])
# print(list1)
#
# # Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer
#
# # Method 1
# arr = [2,4,6,8,10,12,14,16,18,20]
# n= 10
# d = 3
# for i in range(d):
#     temp = arr[0]
#     for j in range(n-1):
#         arr[j] = arr[j+1]
#     arr[n-1] = temp
# print(arr)
#
# # Method 2
# arr = [2,4,6,8,10,12,14,16,18,20]
# n= 10
# d = 3
# arr1 = arr[d:] + arr[:d]
# print(arr1)
#
#
#
# def rotate_array(A,D,N):
#     return A[D:] + A[:D]
# A = [1,2,3,4,5]
# D = 2
# N = 5
# print(rotate_array(A,D,N))
#
# # Method 3
# arr = [2,4,6,8,10,12,14,16,18,20]
# n= 10
# d = 3
#
# class Solution:
#     def rotate_array(self, A,D,N):
#         while D > 0:
#             temp = A[0]
#             for j in range(N-1):
#                 A[j] = A[j+1]
#             A[N-1] = temp
#             D -= 1
#         return A
# s = Solution()
# arr = [1,2,3,4,5]
# d = 2
# n = 5
# print(s.rotate_array(arr,d,n))
#
# # Maximum Index
# # Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
#
# # Method 1
# arr = [34,8,10,3,2,80,30,33,1]
# n = 9
# max = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] <= arr[j]:
#             max = max(max,j-i)
# print(max)
#
# # Method 2
# arr = [34,8,10,3,2,80,30,33,1]
# n = 9
# max = 0
# for i in range(n):
#     for j in range(n-1,i,-1):
#         if arr[i] <= arr[j]:
#             max = max(max,j-i)
# print(max)
#
# # Method 3
# arr = [34,8,10,3,2,80,30,33,1]
# n = 9
# max = 0
# i = 0
# j = n-1
# while i < j:
#     if arr[i] <= arr[j]:
#         max = max(max,j-i)
#         j -= 1
#     else:
#         i += 1
# print(max)
#
# # Contains Duplicate
# # Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# def contains_duplicate(nums):
#     return len(nums) != len(set(nums))
#
# nums = [1,2,3,4,5,6,7,8,9,1]
# print(contains_duplicate(nums))
#
# # Method 2
# def contains_duplicate(nums):
#     dict = {}
#     for i in nums:
#         if i in dict:
#             return True
#         else:
#             dict[i] = 1
#     return False
# nums = [1,2,3,4,5,6,7,8,9,1]
# print(contains_duplicate(nums))
#
# # Vailid Anagram
# # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# def is_anagram(s,t):
#     return sorted(s) == sorted(t)
# s = "anagram"
# t = "nagaram"
# print(is_anagram(s,t))
#
# # Two Sum
# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# def two_sum(nums,target):
#     dict = {}
#     for i in range(len(nums)):
#         if target - nums[i] in dict:
#             return [dict[target-nums[i]],i]
#         else:
#             dict[nums[i]] = i
# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums,target))
#
# # Method 2
# def two_sum(nums,target):
#     dict = {}
#     for i in range(len(nums)):
#         if nums[i] in dict:
#             return [dict[nums[i]],i]
#         else:
#             dict[target-nums[i]] = i
# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums,target))

# FInd Botom left Tree Value
# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# class Solution:
#     def findBottomLeftValue(self, root):
#         queue = [root]
#         while queue:
#             node = queue.pop(0)
#             if node.right:
#                 queue.append(node.right)
#             if node.left:
#                 queue.append(node.left)
#         return node.val


# Even Odd Tree
# A binary tree is named Even-Odd if it meets the following conditions:
#The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
# class Solution:
#     def isEvenOddTree(self, root):
#         queue = [root]
#         level = 0
#         while queue:
#             prev = None
#             for i in range(len(queue)):
#                 node = queue.pop(0)
#                 if level % 2 == 0:
#                     if node.val % 2 == 0 or (prev and prev >= node.val):
#                         return False
#                 else:
#                     if node.val % 2 != 0 or (prev and prev <= node.val):
#                         return False
#                 prev = node.val
# #                 if node.left:
# #                     queue.append(node.left)
# #                 if node.right:
# #                     queue.append(node.right)
# #             level += 1
# #         return True
# #
# #
# # # Create a DataFrame from a List of Lists
# # import pandas as pd
# # data = [['Alex',10],['Bob',12],['Clarke',13]]
# # df = pd.DataFrame(data,columns=['Name','Age'])
# # print(df)
# #
# #
# # # Get the size of a DataFrame
# # import pandas as pd
# # def getDataframeSize(players):
# #     return players.shape
# #
# # # Display the first 3 rows of a DataFrame
# # import pandas as pd
# # def displayFirstThreeRows(players):
# #     return players.head(3)
# #
# # # A company plans to provide its employees with a bonus.
# # #
# # # Write a solution to create a new column name bonus that contains the doubled values of the salary column.
# # #
# # # The result format is in the following example
# #
# # import pandas as pd
# # def addBonusColumn(salary):
# #     salary['bonus'] = salary['salary'] * 2
# #     return salary
# #
#
#
# # Maximum Odd Binary Number
# # Given a binary string s, that contains at least one '1'.
# #You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
#
# # Return a string representing the maximum odd binary number that can be created from the given combination.
# #
# # Note that the resulting string can have leading zeros.
#
# # Contest 125
# # Minimum Opeartion to Exceed Threshold Value 1
# # You are given a 0-indexed integer array nums and an integer k.
# # In one opeation, you can remove one occurrence of the smallest element of nums.
# # Return the minimum number of operations needed to remove all occurrences of the smallest element of nums such that the sum of the remaining elements is greater than or equal to k.
#
# # Contest 125
# # nums = [2,11,10,1,3], k = 10
# # Output: 3
#
# # Input: nums = [1,1,2,4,9], k = 1
# # Output: 0
#
# # Input: nums = [1,1,2,4,9], k = 9
# # Output: 4
#
# # def min_operations(nums, k):
# #     nums.sort()
# #     operations = 0
# #     for num in nums:
# #         if num < k:
# #             operations += 1
# #             nums.remove(num)
# #         else:
# #             break
# #     return operations
# # nums = [1,1,2,4,9]
# # k = 9
# # print(min_operations(nums,k))
#
# # Contest 125
# # Minimum Opeartion to Exceed Threshold Value 2
# # You are given a 0-indexed integer array nums, and an integer k.
# #
# # In one operation, you will:
# #
# # Take the two smallest integers x and y in nums.
# # Remove x and y from nums.
# # Add min(x, y) * 2 + max(x, y) anywhere in the array.
# # Note that you can only apply the described operation if nums contains at least two elements.
# #
# # Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
# # Constraints:
# #
# # 2 <= nums.length <= 2 * 105
# # 1 <= nums[i] <= 109
# # 1 <= k <= 109
# # The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to k.
#
# from heapq import heapify, heappop, heappush
#
# def min_operations(nums, k):
#     heapify(nums)  # Convert the array into a min heap in-place
#     operations = 0
#
#     while nums[0] < k:
#         if len(nums) < 2:
#             break
#         x = heappop(nums)  # Remove the smallest element x from the heap
#         if x >= k:
#             break  # Break if the smallest element x is already greater than or equal to k
#         y = heappop(nums)  # Remove the next smallest element y from the heap
#         new_num = x + 2 * y  # Calculate the new element to insert
#         heappush(nums, new_num)  # Insert the new element into the heap
#         operations += 1
#
#     return operations
#
# # Test cases
# nums1 = [2, 11, 10, 1, 3]
# k1 = 10
# print(min_operations(nums1, k1))  # Output: 2
#
# nums2 = [1, 1, 2, 4, 9]
# k2 = 20
# print(min_operations(nums2, k2))  # Output: 4
#
# # Remove Nth Node From End of List
# # Given the head of a linked list, remove the nth node from the end of the list and return its head.
# # Follow up: Could you do this in one pass?
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0)
#         dummy.next = head
#         first = second = dummy
#         for i in range(n + 1):
#             first = first.next
#         while first:
#             first = first.next
#             second = second.next
#         second.next = second.next.next
#         return dummy.next
#
# # Two Pointers Approach
#
#
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
#
# def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
#     fast = head
#     for _ in range(n):
#         if not fast:
#           return None
#         fast = fast.next
#
#     slow = head
#     prev = None
#     while fast:
#         prev = slow
#         slow = slow.next
#         fast = fast.next
#
#     if not prev:
#         return head.next
#     else:
#         prev.next = slow.next
#     return head
#
#
#
#
# # Bag of Tokens
# You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.
# Your goal is to maximize your total score by potentially playing each token in one of two ways:
# If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
# If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
# Return the maximum score you can achieve after playing any number of tokens.
# Note that you may play the tokens in any order.
# Example 1:
# Input: tokens = [100], power = 50
# Output: 0
# Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).
# Example 2:
# Input: tokens = [100,200], power = 150
# Output: 1
# Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.
#
# There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

def bagOfTokensScore(tokens, power):
    tokens.sort()
    score = 0
    max_score = 0
    left, right = 0, len(tokens) - 1

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score
print(bagOfTokensScore([100,200,300,400],200))





