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
        """
        Method1: Binary Search find one target, and then slide window to find left and right
        """
        # def binarySearch(nums, target):
        #     l,r = 0, len(nums)-1
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] > target:
        #             r = mid-1
        #         else:
        #             l = mid+1
        #     return -1
        
        # idx = binarySearch(nums, target)
        # if idx == -1:
        #     return [-1,-1]
        # left, right = idx, idx
        # while left >= 0 and nums[left] == target:
        #     left -= 1
        # while right < len(nums) and nums[right] == target:
        #     right += 1
        # return [left+1, right-1]

        """
        Method2: Find Left border and Right border seperately
        """
        def findLeft(nums, target):
            leftBorder = -2
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    leftBorder = r
            return leftBorder
        def findRight(nums, target):
            rightBorder = -2
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
                    rightBorder = l
            return rightBorder
        
        left, right = findLeft(nums, target), findRight(nums, target)
        if left == -2 or right == -2:
            return [-1,-1]
        elif right - left > 1: 
            return [left+1, right-1]
        else:
            return [-1,-1]


                


# @lc code=end

