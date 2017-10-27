# 阶梯训练3 Linear Data Structure I
## 1. LintCode_482 链表转数组
**描述：**
```
将一个链表转换为一个数组。
```

**样例：**
```
给出链表 1->2->3->null, 返回 [1,2,3].
```

**Code:**
```
def toArrayList(self, head):
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res
```

## 2. LintCode_225 在链表中找结点
**描述：**
```
在链表中找值为 value 的节点，如果没有的话，返回空。
```

**样例：**
```
给出 1->2->3 和 value = 3, 返回最后一个节点 last node.

给出 1->2->3 和 value = 4, 返回空。
```

**Code:**
```
def findNode(self, head, val):
    while head is not None:
        if head.val == val:
            return head
        head = head.next
    return None
```

## 3. LintCode_219 在排序链表中插入一个结点
**描述：**
```
在链表中插入一个节点。
```

**样例：**
```
给出一个链表 1->4->6->8 和 val = 5.。

插入后的结果为 1->4->5->6->8。
```

**Code:**
```
def insertNode(self, head, val):
    node = ListNode(val)
    dummy = ListNode(0)
    dummy.next = head
    head = dummy

    while head.next != None and head.next.val <= val:
        head = head.next
    node.next = head.next
    head.next = node

    return dummy.next
```



## 4. LintCode_452 删除链表中的元素
**描述：**
```
删除链表中等于给定值val的所有节点。
```

**样例：**
```
给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。
```

**Code：**
```
def removeElements(self, head, val):
    if head == None:
        return head
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    while head:
        if head.val == val:
            prev.next = head.next
            head = prev
        else:
            prev = head
            head = head.next
    return dummy.next
```


## 5. LintCode_241 转换字符串到整数(容易版)
**描述：**
```
给一个字符串, 装换为整数. 你可以假设这个字符串是一个有效的整数的字符串形式， 且范围在32位整数之间 (-231 ~ 231-1)。
```

**样例：**
```
给出 "123", 返回 123.
```

**COde：**
```
def stringToInteger(self, str):
    # solution 2
    num, sig = 0, 1

    if str[0] == '-':
        sig = -1
        str = str[1:]

    for c in str:
        num = num * 10 + ord(c)- ord('0')

    return num * sig

    """
    #solution 1
    return int(str)
    """
```

## 6. LintCode_415 有效回文串
**描述：**
```
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。
```

**样例：**
```
"A man, a plan, a canal: Panama" 是一个回文。

"race a car" 不是一个回文。
```

**Code：**
```
def isPalindrome(self, s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalpha() and not s[left].isdigit():
            left += 1
        while left < right and not s[right].isalpha() and not s[right].isdigit():
            right -= 1
        if left < right and  s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

## 7. LintCode_174 删除链表中的倒数第n个节点
**描述：**
```
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
```

**样例：**
```
给出链表1->2->3->4->5->null和 n = 2.

删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.
```

**Code：**
```
def removeNthFromEnd(self, head, n):
    len = 0
    curr1 = head
    while curr1:
        len += 1
        curr1 = curr1.next

    dummy = ListNode(0)
    dummy.next = head
    head = dummy
    for i in range(len - n):
        head = head.next
    head.next = head.next.next

    return dummy.next
```

## 8. LintCode_165 合并两个排序链表
**描述：**
```
将两个排序链表合并为一个新的排序链表
```

**样例：**
```
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
```

**Code：**
```
def mergeTwoLists(self, l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if not l1:
        curr.next = l2
    else:
        curr.next = l1

    return dummy.next
```

## 9. LintCode_228 链表的中点
**描述：**
```
找链表的中点。
```

**样例：**
```
链表 1->2->3 的中点是 2。

链表 1->2 的中点是 1。
```

**Code:**
```
def middleNode(self, head):
    if head is None:
        return None

    slow = head
    fast = slow.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
```

