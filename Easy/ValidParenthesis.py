class Solution(object):
   def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        #string cannot be odd
        if(len(s)%2!=0):
            return False
        #string has to start with opening parenthesis
        if s[0]!="(" and s[0]!="{" and s[0] != "[":
            return False
        
        stack = []
        
        for char in s:
            if char=="(" or char=="{" or char=="[":
                stack.append(char)
            
            else:
                #make sure we cant pop from an empty stack
                if len(stack)==0:
                    return False
                
                #for each closing character, pop element from stack            
                if char == ")" and stack.pop()!="(":
                    return False
                if char == "}" and stack.pop()!="{":
                    return False
                if char == "]" and stack.pop()!="[":
                    return False
        
        if len(stack)!=0:
            return False
        
        else:
            return True
    
        