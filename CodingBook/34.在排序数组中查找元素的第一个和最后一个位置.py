#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_s(ns,target):
            l,r = 0,len(ns)-1
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    return mid
                elif nums[]
# @lc code=end

