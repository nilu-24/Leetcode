class Solution(object):
    def search(self, nums, target):
        
        #if empty, return -1
        if len(nums)==0:
            return -1
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            middle = (left + right)//2
            
            if nums[middle]==target:
                return middle
            
            elif nums[middle] < target:
                #target has to be on the right side
                left = middle+1
            
            else:
                right = middle-1
                
        return -1
            
"""
TC - O(logN)
SC - O(1)

"""