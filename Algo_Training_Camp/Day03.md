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
### 