

"""
LEETCODE 1

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""


class Solution(object):
    def twoSum(self, nums, target):
        
        d = {} #dict to store num : index
        
        #looping through the list
        for i in range(len(nums)):
            #for each number, if target-num is in the keys
            if target-nums[i] in d.keys():
                #return the current index and the index of the target-i
                return [i,d[target-nums[i]]] 
            
            
            #add the number as key in the hashmap
            #if the key was already there, the index value gets updated to the 
            #next occurance of the number the same index is not repeated
        
            d[nums[i]] = i
    
        """
        Time Complexity - O(n)
        Space Complexity - O(n)
        
        Naive approach could be for each num, compare with rest of the num
        and see if they sum to target.
        
        But O(n^2)
        
        """
        