#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r = 0, num
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l = mid+1
            else:
                r = mid-1
        return False
# @lc code=end

