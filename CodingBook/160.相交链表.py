#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # length of headA and headB
        lengthA, lengthB = 0, 0
        cur = headA
        while cur is not None:
            lengthA += 1
            cur = cur.next
        cur = headB
        while cur is not None:
            lengthB += 1
            cur = cur.next
        # 将两个指针移动到两个链表的相同位置，保证后续剩下的节点数量相同
        nodeA, nodeB = headA, headB
        if lengthA > lengthB:
            while lengthA > lengthB:
                nodeA = nodeA.next
                lengthA -= 1
        else:
            while lengthB > lengthA:
                nodeB = nodeB.next
                lengthB -= 1
        # 比较两个指针对应节点是否相等
        while nodeA is not None and nodeB is not None:
            if nodeA == nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
        return None
    


# @lc code=end

