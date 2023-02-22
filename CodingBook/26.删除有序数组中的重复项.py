#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                slow += 1
        
        return slow+1
                


# @lc code=end

