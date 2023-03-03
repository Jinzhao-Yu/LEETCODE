#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(next = head) # 虚拟头节点
        cur = dummy
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next # 去除虚拟头节点
   
# @lc code=end

