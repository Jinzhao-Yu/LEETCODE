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
- 快慢指针先找到倒数第N个节点
- 另存一下目标节点的上一个节点，然后直接删除当前节点
- 注意使用虚拟头节点避免出现删除第一个节点或者空链表是报错
```python
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
```
### LC