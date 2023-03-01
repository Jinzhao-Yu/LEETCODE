# Day01｜数组基础｜二分查找｜双指针
## Binary Search 二分查找
- 边界Case需要注意
- 区间选择：左开右闭、左闭右开、左闭右闭、左开右开，注意保持一致
- ```mid = left + (right-left)//2```
- 二分查找的时间复杂度为$O(logN)$
### LC704.二分查找
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return -1
```
### LC34.在排序数组中查找元素的第一个和最后一个位置
#### 方法一：暴力解法，分别找到左边界和右边界
```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Method1: Find Left border and Right border seperately
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

```
#### 方法二：先找到一个目标元素，再利用滑动窗口找到左右边界
```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Method2: Binary Search find one target, and then slide window to find left and right
        """
        def binarySearch(nums, target):
            l,r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        idx = binarySearch(nums, target)
        if idx == -1:
            return [-1,-1]
        left, right = idx, idx
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left+1, right-1]
```
### LC35.搜索插入位置
```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return l
```
## Two Pointers 双指针
- 快慢指针，快的理解为一直向后移动，慢的作为一个坐标进行后续操作
### LC27.移除元素
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow
```