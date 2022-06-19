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


        # TC - O(N)
        # SC - O(N)
    
        # could also be done using a hash map
        # TC - O(N)
        # SC - O(N)

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
        
        OpentoClose  ={"(":")","{":"}","[":"]"} #using a map to map opening to closing        
        
        for char in s: #loop through each character
            if char in OpentoClose.keys(): #if it is an opening tag,
                stack.append(char) #add to stack
                
            else:
                if len(stack)==0: #ensure it so that we dont pop from empty stack
                    return False
                #for each closing character, pop element from stack            
                if char!=OpentoClose.get(stack.pop(),0): #if the closing parenthesis do not have its opening match
                    return False
        
        if len(stack)!=0: #if any char remains
            return False
        
        else: #all clear
            return True