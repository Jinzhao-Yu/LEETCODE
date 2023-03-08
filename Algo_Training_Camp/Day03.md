# Day03｜链表Linked List
## 类型
- 单链表：每个节点只包含head与next\
![image1](https://img-blog.csdnimg.cn/20200806194529815.png)
- 双链表：每一个节点有两个指针域，一个指向下一个节点next，一个指向上一个节点prev，因此双链表既可以向前查询也可以向后查询\
![image2](https://img-blog.csdnimg.cn/20200806194559317.png)
- 循环链表：链表首尾相连\
![image3](https://img-blog.csdnimg.cn/20200806194629603.png)
## 定义一个链表Class
```python
# 单链表
class ListNode{
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
}
```
## 链表操作
- 删除节点：只需要将上一个节点的next直接跳过需要删除的节点，连接到下一节点即可
- 添加节点：在两个节点之间加入一个节点，只需要直接改变前节点的next和添加节点的next即可

![image4](https://img-blog.csdnimg.cn/20200806195200276.png)

### LC203.移除链表元素
- 建立虚拟头节点以保证遍历每一个节点val
- return时需要去掉虚拟头节点
```python
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
```
### LC707.设计链表
- 覆盖了链表的基本操作，需要写出5种函数，十分全面
- 要点是在`__init__`中就可以设置好虚拟头节点，方便后续的所有操作
- 设置`self.size`便于后续计算链表的长度
```python
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
```
### LC206.反转链表
- 迭代法和递归法两种方式
- 迭代法：使用双指针，分别指向当前节点cur和上一个节点prev，每次进行的操作时将cur的next变为prev，并使用temp将原来的next存下来用作下一步的cur，直到最后一个节点
- 需要注意的是，初始化prev时不要设置为一个新的ListNode，否则在输出时会在结尾额外输出一个None
```python
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
        cur = head
        prev = None # 避免输出尾部的None，不要把这里初始化为ListNode
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        return prev
```
- 递归法：重复调用函数本身形成递归
- 从后向前递归：将一个节点的next部分先使用函数完成反转，再将这个节点连接在反转后结果的最后，注意边界情况
```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归法
        if head is None or head.next is None: # 边界case
            return head
        temp = self.reverseList(head.next) # 将当前节点的后面部分全部反转
        head.next.next = head # next指向的节点的next，就是将head接在结果的最后
        head.next = None # 断开原有的链接
        return temp
```