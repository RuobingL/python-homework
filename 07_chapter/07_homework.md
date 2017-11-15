# 阶梯作业7 Principle and Application of Sorting Algorithm
## LintCode_463 整数排序
**描述：**
```
给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。
```
**样例：**
```
对于数组 [3, 2, 1, 4, 5], 排序后为：[1, 2, 3, 4, 5]。
```

**Code：**
```
def sortIntegers(self, A):
    for i in range(len(A) - 1, 0 , -1):
        # print i
        for j in range(i):
            print j
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A
```

## LintCode_464 整数排序II
**描述：**
```
给一组整数，按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
```
**样例：**
```
给出 [3, 2, 1, 4, 5], 排序后的结果为 [1, 2, 3, 4, 5]。
```

**Code：**
```
def sortIntegers2(self, A):
    len_a = len(A)
    temp = [0 for _ in range(len_a)]
    self.merge_sort(A, 0, len_a - 1, temp)

def merge_sort(self, A, start,  end, emp):

    if start >= end:
        return

    mid = start + (end - start) / 2
    self.merge_sort(A, start, mid, temp)
    self.merge_sort(A, mid + 1, end, temp)
    self.merge(A, start, end, temp)

def merge(self, A, start, end, temp):
    mid = start + (end - start) / 2
    (TODO: yelin)
    left, right = start, mid + 1
    index = start

    while left <= mid and right <= end:
        if A[left] < A[right]:
            temp[index] = A[right]
            left += 1
            right += 1
        else:
            temp[index] = B[left]
            left += 1
            right += 1

    while left <= mid:
        temp[index] = A[left]
        index += 1
        left += 1

    while right <= mid:
        temp[index] = A[right]
        index += 1
        right += 1
```

## LintCode_173 链表插入排序
**描述：**
```
用插入排序对链表排序
```
**样例：**
```
Given 1->3->2->0->null, return 0->1->2->3->null
```

**Code：**
```
def insertionSortList(self, head):
    dummy = ListNode(val = -sys.maxint - 1)

    while head:
        temp = dummy
        next = head.next
        while temp.next and temp.next.val < head.val:
            temp = temp.next

        head.next = temp.next
        temp.next = head

        head = next

    return dummy.next
```

## LintCode_184 最大数
**描述：**
```
给出一组非负整数，重新排列他们的顺序把他们组成一个最大的整数。
```
**样例：**
```
给出 [1, 20, 23, 4, 8]，返回组合最大的整数应为8423201。
```

**Code：**
```
def largestNumber(self, nums):
    nums = sorted(nums, cmp = lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1)
    print nums
    ans_nums = ''.join(str(x) for x in nums)
    if ans_nums == '0' * len(nums):
        return '0'
    else:
        return ans_nums
```

## LintCode_148 颜色分类
**描述：**
```
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。
```
**样例：**
```
给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。
```

**Code：**
```
def sort(self, A, flag, index):
    start, end = index, len(A) - 1
    while start <= end:
        while start <= end and A[start] == flag:
            start += 1
        while start <= end and A[end] != flag:
            end -= 1
        if start <= end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
    return start

def sortColors(self, A):
    self.sort(A, 1, self.sort(A, 0, 0))
```

## LintCode_143 排颜色II
**描述：**
```
给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。
```
**样例：**
```
给出colors=[3, 2, 2, 1, 4]，k=4, 你的代码应该在原地操作使得数组变成[1, 2, 2, 3, 4]
```

**Code：**
```
def sortColors2(self, colors, k):
    self.sort(colors, 0, 0, k)
    

def sort(self, A, flag, index, K):
    if flag >= K:
        return
    
    start, end= index, len(A) - 1
    while start <= end:
        while start <= end and A[start] == flag:
            start += 1
        while start <= end and A[end] != flag:
            end -= 1
        if start <= end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
    self.sort(A, flag + 1, start, K)
```

## LintCode_139 最接近零的子数组和
**描述：**
```
给定一个整数数组，找到一个和最接近于零的子数组。返回第一个和最有一个指数。你的代码应该返回满足要求的子数组的起始位置和结束位置
```
**样例：**
```
给出[-3, 1, 1, -3, 5]，返回[0, 2]，[1, 3]， [1, 1]， [2, 2] 或者 [0, 4]。
```

**Code：**
```
class Node:
    def __init__(self, _value, _pos):
        self.value = _value
        self.pos = _pos
    
    def __cmp__(self, other):
        if self.value == other.value:
            return self.pos - other.value
        return self.value - other.value
    
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        s = []
        s.append(Node(0, -1))
        sum = 0
        for x in xrange(len(nums)):
            sum += nums[x]
            s.append(Node(sum, x))

        s = sorted(s)
        results= [0,0]
        ans = 1000000000000
        for i in xrange(len(s)-1):
            if s[i+1].value - s[i].value < ans or \
                s[i+1].value - s[i].value == ans and \
                min(s[i+1].pos, s[i].pos) + 1 < results[0]:
                ans = s[i+1].value - s[i].value
                results[0] = min(s[i+1].pos, s[i].pos) + 1          
                results[1] = max(s[i+1].pos, s[i].pos)

        return results
```

## LintCode_98 链表排序
**描述：**
```
给定一个字符串 s 和一个 非空字符串 p ，找到在 s 中所有关于 p 的字谜的起始索引。
字符串仅由小写英文字母组成，字符串 s 和 p 的长度不得大于 40,000。
输出顺序无关紧要。
```
**样例：**
```
给出字符串 s = "cbaebabacd" p = "abc"
返回 [0, 6]

子串起始索引 index = 0 是 "cba"，是"abc"的字谜.
子串起始索引 index = 6 是 "bac"，是"abc"的字谜.
```

**Code：**
```
def findAnagrams(self, s, p):
    ans = []
    sum = [0] * 30
    plength = len(p)
    slength = len(s)
    for i in range(plength):
        sum[ord(p[i]) - ord('a')] += 1
    start = 0
    end = 0
    matched = 0
    while end < slength:
        if sum[ord(s[end]) - ord('a')] >= 1:
            matched += 1
        sum[ord(s[end]) - ord('a')] -= 1
        end += 1
        if matched == plength:
            ans.append(start)
        if end - start == plength:
            if sum[ord(s[start]) - ord('a')] >= 0:
                matched -= 1
            sum[ord(s[start]) - ord('a')] += 1
            start += 1

    return ans
```

## LintCode_5 第k大元素
**描述：**
```
在数组中找到第k大的元素
```
**样例：**
```
给出数组 [9,3,2,4,8]，第三大的元素是 4

给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推
```

**Code：**
```
def kthLargestElement(self, k, A):
    n = len(A)
    k -= 1
    
    return self.partitionHelper(A, 0, n - 1)    
    
def partitionHelper(self, A, s, e):
    p, q = s + 1, e
    while p <= q:
        if A[p] > A[s]:
            p += 1
        else:
            A[p], A[q] = A[q], A[p]
            q -= 1
    A[s], A[q] = A[q], A[s]
    
    m = q
    if m == k:
        return A[m]
    elif m < k:
        return partitionHelper(A, m + 1, e)
    else:
        return partitionHelper(A, a, m - 1)
```
