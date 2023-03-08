# Day04｜链表Linked List
### LC24.两两交换链表中的节点
- 递归法，运用跟Day03反转链表相似的方法
```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temp = self.swapPairs(head.next.next)
        res = head.next
        res.next = head
        head.next = temp
        return res
```
### LC19.删除链表的倒数第N个节点
