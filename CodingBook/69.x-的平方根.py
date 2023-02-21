#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid-1
            else:
                l = mid+1
        
        return l-1
# @lc code=end

