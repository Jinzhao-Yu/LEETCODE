#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口
        idx1 = 0
        length = float('inf')
        sum = 0
        for idx2 in range(len(nums)):
            sum += nums[idx2]
            while sum >= target:
                length = min(length, idx2-idx1+1)
                sum -= nums[idx1]
                idx1 += 1
        if length == float('inf'):
            return 0
        else:
            return length
# @lc code=end

