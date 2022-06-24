class Solution(object):
    def isPalindrome(self, x):
        
        #if num negative, return false
        """
        :type x: int
        :rtype: bool
        """
        #convert int to string
        #compare the start and end postitions
        
        if x <0:
            return False
        
        x_str = str(x)
        
        #using a two pointer approach
        
        start = 0
        end = len(x_str)-1
        
        while(start<end):
            if x_str[start]!=x_str[end]:
                return False
            start+=1
            end-=1
            
        return True
    
    
    