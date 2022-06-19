"""
LEETCODE 242 - Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

#sorting the list and then comparing 
#time complexity O(nlogn) for the sorting
#space maybe O(n) for using lists

class Solution(object):
    def isAnagram(self, s, t):
        
        #input - two strings
        #output - boolean
        
        #CASE 1 - if the strings are of different lengths
        
        if len(s)!=len(t):
            return False
        #CASE 2 - if the strings are just a character 
        
        if len(s)==1 and len(t)==1:
            if s==t:
                return True
        
        #converting the strings to a list
        
        s_list = list(s)
        t_list = list(t)
        
        #sort the lists
        
        s_list.sort()
        t_list.sort()
        
        if s_list == t_list:
            return True
        else:
            return False
        
#METHOD 2 - using dictionaires

#time complexity O(n)
#space complexity O(n)

class Solution2(object):
    def isAnagram(self, s, t):

        if len(s)!=len(t):
            return False
        
        #we need to keep track of the counts of each letter
        #map letter : count
        #compare the dicts
        mapS={}
        mapT ={}
        #d.get(key,0) --> get the value of the key and if key doesnt exist, return 0
        for i in range(len(s)):
            mapS[s[i]] = 1+mapS.get(s[i],0)
            mapT[t[i]] = 1+mapT.get(t[i],0)
        
        for key in mapS:
            if mapS[key]!=mapT.get(key,0): #again, we aren't sure if the same key might exist
                return False
        
        return True
    
        

s = Solution2()

print(s.isAnagram("anagram","nagaram"))
