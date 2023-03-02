#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        x,y = 0,0 # start point of a loop
        num = 1
        for loop in range(1, n//2+1): # 每次循环都是完成最外层的赋值
            for i in range(y,n-loop): # left to right
                res[x][i] = num
                num += 1
            for i in range(x,n-loop): # up to down
                res[i][n-loop] = num
                num += 1
            for i in range(y,n-loop): # right to left
                res[n-loop][n-1-i] = num
                num += 1
            for i in range(x,n-loop): # down to up
                res[n-1-i][y] = num
                num += 1
            x += 1
            y += 1
        if n%2 == 0:
            return res
        else: 
            res[n//2][n//2] = num
            return res
# @lc code=end

