
"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """  
        #move all the non zero values in front
        #fill the remaining array with zeroes
        
        indexCount = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[indexCount]=nums[i]
                indexCount+=1
        
        for j in range(indexCount,len(nums)):
            nums[j]=0
        
        return 