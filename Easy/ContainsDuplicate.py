"""
LEETCODE 217
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

"""

class Solution(object):
    def containsDuplicate(self, nums):
        #input - an array
        #output - a boolean

        # CASE 1: if there is only one element in the array
        if len(nums)==1:
            return False
        # CASE 2: if the array is empty
        
        if len(nums)==0:
            return False
        
        #CASE 3: if there are more than 1 elements in the array
        # convert the array to a set
        
        nums_set = set(nums) #convert the list to a set to make sure only unique elements are kept
        
        if len(nums_set)==len(nums): #if no duplicates, then they will be same
            return False #so return False
        else:
            return True #there will be atleast some duplicates

# TESTING

nums  = [1,2,3,4,5,6]
nums2 = [1,2,2,2,4,7]

s = Solution()

result1 = s.containsDuplicate(nums)
result2 = s.containsDuplicate(nums2)

str1 = "TestCase 1: "
str2 = "TestCase 2: "

if result1 == False:
    str1+="Passed"
else:
    str1+="Failed"

if result2 ==True:
    str2+="Passed"
else:
    str2+="Failed"

print(str1 + "\n" + str2)

    

"""
3 ways to solve it

1. Brute force - for each element, check all other elements if there is any duplicate
Time Complexity - O(n^2)
Space Complexity - O(1)

2. Sort the array, then compare each element with the next, two duplicates will be side by side
Time Complexity - O(nlogn) [sorting is the bottleneck]
Space Complexity - O(1)

3. Use a hashset
create a hashset and add each element in the hashset
then check if the element exists in the hashset
if exist, return True

num_set = set()
        
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

Time Complexity - O(n)
Space Complexity - O(n)

The last solution is the most optimum

"""
