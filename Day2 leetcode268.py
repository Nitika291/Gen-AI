class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)

"""
Input: nums = [3,0,1]
Output: 2
"""
