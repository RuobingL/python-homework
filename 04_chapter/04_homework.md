# 阶梯训练 线性数据结构 II Linear Data Structure II

## LintCode_495 实现栈
**描述：**
```
实现一个栈，可以使用除了栈之外的数据结构
```

**样例：**
```
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
```

**Code:**
```
class Stack:
    def __init__(self):
        self.queue = []
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        return self.queue.pop()

    """
    @return: An integer
    """
    def top(self):
        return self.queue[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.queue == []
```

## LintCode_423 有效的括号队列
**描述：**
```
给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。
```

**样例:**
```
括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。
```

**Code:**
```
def isValidParentheses(self, s):
    res = ['#']
    for item in s:
        if res[-1] == '(' and item == ')':
            res.pop()
        elif res[-1] == '{' and item == '}':
            res.pop()
        elif res[-1] == '[' and item == ']':
            res.pop()
        else:
            res.append(item)

    if len(res) == 1:
        return True
    else:
        return False
```

## LintCode_40 用栈实现队列
**描述：**
```
正如标题所述，你需要使用两个栈来实现队列的一些操作。

队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。

pop和top方法都应该返回第一个元素的值。
```

**样例：**
```
比如push(1), pop(), push(2), push(3), top(), pop()，你应该返回1，2和2
```

**Code:**
```
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        self.adjust()
        return self.stack2[len(self.stack2) - 1]

    def pop(self):
        self.adjust()
        return self.stack2.pop()

```
