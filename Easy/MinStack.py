"""
LEETCODE 155
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

class MinStack(object):

    def __init__(self):
        self.stack = [] #one stack to store the numbers
        self.minStack = [] #another one to store the minimum values
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #if both the stacks are empty, add the number to both of the stacks
        if len(self.stack)==0 and len(self.minStack)==0:
            self.stack.append(val)
            self.minStack.append(val)
        #or else
        #add the value to the normal stack
        else:
            self.stack.append(val)
            #if the value is smaller than the last element in the minstack, add it
            if val < self.minStack[-1]:
                self.minStack.append(val)
            #if the value is equal to or larger
            elif val >= self.minStack[-1]:
                self.minStack.append(self.minStack[-1])
                #just add the same prev value to the min
            
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:

s = MinStack()

s.push(-2)
s.push(0)
s.push(-3)

print(s.stack)
print(s.minStack)