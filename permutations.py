'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''

#SOLUTION

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li,res = [],[]
        def backtrack():
            if len(li)==len(nums):
                res.append(li[:])
                return 
            
            for i in nums:
                if i not in li:
                    li.append(i)
                    backtrack()
                    li.pop()
        backtrack()
        return res
