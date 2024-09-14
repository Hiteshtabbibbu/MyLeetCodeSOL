'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
'''

#SOLUTION

class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def isvalid(a, b, c):
            return a != b and a != c and b != c
        
        h = {nums[i]: i for i in range(len(nums))}
        s = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                req = 0 - nums[i] - nums[j]
                if req in h and isvalid(i, j, h[req]):
                    t = tuple(sorted([nums[i], nums[j], req]))
                    s.add(t)
        
        return s
        
