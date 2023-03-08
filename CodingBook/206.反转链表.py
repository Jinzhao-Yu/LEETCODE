#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代法/双指针
        # cur = head
        # prev = None # 避免输出尾部的None，不要把这里初始化为ListNode
        # while cur is not None:
        #     temp = cur.next
        #     cur.next = prev
        #     prev, cur = cur, temp
        # return prev
    
        # 递归法
        if head is None or head.next is None:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
        
# @lc code=end


