# Day02｜双指针｜滑动窗口｜模拟
## Two Pointers 双指针
- 与Day01相同，双指针用于定位，实现 $O(N)$的时间复杂度
### LC977.有序数组的平方
- 暴力解法：直接把所有元素平方，然后重新排序
    - 排序：[十大排序方法]()
- 为了实现时间复杂度 $O(N)$，需要另外创建一个新的空数组，用来储存平方后的结果
- 由于数组为有序数组，但存在正负值，因此位于数组左右两侧的元素平方后可能为最大值，双指针分别从左右向内收缩，直到重合
- 将左右指针元素的平方数较大值从后向前存储在新数组中，并将对应的指针向内收缩以对比所有的平方数
```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
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
```
## Sliding Window 滑动窗口
- 滑动窗口本质上就是左右边界不断调整，子串的长度也不断调整从而完成遍历
- 注意不能将左右边界分别循环，而是将其中一个作为循环的变量，另一个边界视题目情况进行调整
- 时间复杂度可以降低为 $O(N)$
- **相关题目：LC904, LC76**
### LC209.长度最小的子数组
- 注意滑动窗口内部的元素和可以避免每次都用`sum`函数计算，可以通过上一次计算得到的结果减去去除的元素或加上增加的元素得到
- 另外该方法只能用于非负数组，如果存在负数则无法通过滑动窗口遍历全部可能性，仍需要使用暴力法 $O(N^2)$遍历
```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        idx1 = 0 # 左边界
        length = float('inf') # 初始的最短长度需要设置为一个极大值
        sum = 0 # 设置子串总和的初始值
        for idx2 in range(len(nums)):
            sum += nums[idx2]
            while sum >= target: 
                # 如果子串和大于等于target，可以通过收缩左边界找到是否在该子串内存在更短的符合条件的子串
                length = min(length, idx2-idx1+1) # update长度
                sum -= nums[idx1]
                idx1 += 1
        if length == float('inf'): # 不存在符合条件的子串
            return 0
        else:
            return length
```
## Simulation 模拟
- 模拟实际上不涉及算法内容，需要想清楚整个过程的执行，并用代码表示出来
### LC59.螺旋矩阵 II
- 需要注意的是在循环过程中，不能重复对某一个位置进行赋值，因此需要注意对区间的控制，比如这里就是控制左闭右开区间进行循环操作（下图）\
![image](https://code-thinking-1253855093.file.myqcloud.com/pics/20220922102236.png)
- 按顺序模拟对每一条边的填充
```python
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
            y += 1 # 更新起始点
        if n%2 == 0:
            return res
        else: 
            res[n//2][n//2] = num
            return res
```
- **相关题目：LC54.螺旋矩阵**

**相关题目暂未完成！**