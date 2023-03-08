#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_f, node_s = head, head
        dummyNode = ListNode(next = head)
        prev = dummyNode
        while n > 0:
            node_f = node_f.next
            n -= 1
        while node_f is not None:
            prev = node_s
            node_f, node_s = node_f.next, node_s.next
        prev.next = node_s.next
        return dummyNode.next
    
        
# @lc code=end

