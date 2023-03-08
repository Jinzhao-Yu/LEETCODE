#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先判断是否存在环：快慢指针
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: # 证明存在环
                # 根据数学推导，在head和相遇点分别放置两个指针并同时移动，相遇点为环开始节点
                idx1,idx2 = head,slow
                while idx1 != idx2:
                    idx1 = idx1.next
                    idx2 = idx2.next
                return idx1
        return None
# @lc code=end
