#
# @lc app=leetcode.cn id=707 lang=python
#
# [707] 设计链表
#

# @lc code=start
class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = Node() # 等于是已经创建了一个虚拟头节点！！
        self.size = 0 # Size of Linked List


    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.head.next
        if index < 0 or index >= self.size:
            return -1
        while index > 0:
            index -= 1
            cur = cur.next
        return cur.val


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        add = Node(val)
        add.next = self.head.next
        self.head.next = add
        self.size += 1

        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)
        self.size += 1


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.size:
            self.addAtTail(val)
        elif index < 0:
            self.addAtHead(val)
        elif index > self.size:
            pass
        else:
            prev = self.head
            while index > 0:
                prev = prev.next
                index -= 1
            add = Node(val)
            add.next = prev.next
            prev.next = add
            self.size += 1

        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            pass
        else:
            prev = self.head
            while index > 0:
                prev = prev.next
                index -= 1
            prev.next = prev.next.next
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

