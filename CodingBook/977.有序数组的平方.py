#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Method1: square all elements and then sorted
        """

        """
        Method2: Two pointers, copy a new list with the same size
        """
        res = [None]*len(nums)
        idx1, idx2, idx = 0, len(nums)-1, len(res)-1
        while idx1 <= idx2:
            if nums[idx1]*nums[idx1] >= nums[idx2]*nums[idx2]:
                res[idx] = nums[idx1]*nums[idx1]
                idx1 += 1
            else:
                res[idx] = nums[idx2]*nums[idx2]
                idx2 -= 1
            idx -= 1
        return res
# @lc code=end

