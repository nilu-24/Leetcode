
"""
LEETCODE 344
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

"""

# Approach using two-pointers
#O(1) Space Complexity
#O(n) Time Complexity

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #using a two-pointer approach
        
        start = 0 #starting position
        end = len(s)-1 #ending position
        
        while start < end: #while we reach the middle
            temp = s[start] #store the start element in a variable
            s[start] = s[end] #replace start with end
            s[end] = temp #replace end with start
            
            start+=1 #increment the start index
            end-=1 #decrement the end index
            

 #We could use a stack for O(n) space complexity
#We could also do it recursively, but same O(n) space complexity because of callstack