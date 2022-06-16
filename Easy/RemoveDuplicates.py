
"""
LEETCODE 26 - 
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

"""

def removeDuplicates(nums):

#using a two pointer approach
# first pointer is for all the elements
#second pointer is for tracking the unique indices 
    count = 0#counts the number of unique numbers we have
    index = 0 #where to put the unique elements

    for i in range(len(nums)-1): #start from the first to n-1th element
        if nums[i]!=nums[i+1]: #if the next number is different, 
            count+=1 #that means the ith number is unique so count++
            nums[index] = nums[i] #put the number at the index
            index+=1 #increment the index

    #here, we have left out the last unique number
    #so unqiue numbers will actually be count+1

    count = count +1

    nums[index] = nums[len(nums)-1] #lastly, change the index (count -1) to the last element
    
    return count
            

# this can be done keeping the first element same too!, maybe easier


nums = [1,1,2,2]
print(removeDuplicates(nums))

print(nums)