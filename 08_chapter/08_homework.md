# 阶梯作业8 Training More
## LintCode_628 最大子树
**描述：**
```
给你一棵二叉树，找二叉树中的一棵子树，他的所有节点之和最大。
返回这棵子树的根节点。
```

**样例：**
```
给出如下二叉树

     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5 
返回值为 3 的节点。
```

**Code:**
```
subtree = None
subtreeSum = -sys.maxint - 1

def findSubtree(self, root):
    self.helper(root)
    return self.subtree

def helper(self, root):
    if root is None:
        return 0
        
    sum = self.helper(root.left) + self.helper(root.right) + root.val

    if sum > self.subtreeSum:
        self.subtreeSum = sum
        self.subtree = root

    return sum
```

## LintCode_626 矩形重叠
**描述：**
```
给定两个矩形，判断这两个矩形是否有重叠。

注意事项

l1代表第一个矩形的左上角
r1代表第一个矩形的右下角
l2代表第二个矩形的左上角
r2代表第二个矩形的右下角

保证：l1 != r2 并且 l2 != r2
```

**样例：**
```
给定 l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], 返回 true

给定 l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], 返回 false
```

**Code:**
```
def doOverlap(self, l1, r1, l2, r2):
    if l1.x > r2.x or l2.x > r1.x:
        return False
    
    if l1.y < r2.y or l2.y < r1.y:
        return False
    
    return True
```

## LintCode_604 滑动窗口内数的和
**描述：**
```
给你一个大小为n的整型数组和一个大小为k的滑动窗口，将滑动窗口从头移到尾，输出从开始到结束每一个时刻滑动窗口内的数的和。
```

**样例：**
```
对于数组 [1,2,7,8,5] ，滑动窗口大小k= 3 。
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
返回 [10,17,20]
```

**Code:**
```
def winSum(self, nums, k):
    if k == 0 or nums is None:
        return []
    if k >= len(nums):
        return [sum(nums)]
        
    ans = []
    for i in range(len(nums) - k + 1):
        ans.append(sum(nums[i:i + k]))

    return ans
```

## LintCode_407 加一
**描述：**
```
给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照大小进行排列，最大的数在列表的最前面。
```

**样例：**
```
给定 [1,2,3] 表示 123, 返回 [1,2,4].

给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
```

**Code:**
```
def plusOne(self, digits):
    digits.insert(0,0)
    digits[-1] += 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
    
    if digits[0] == 0:
        digits.remove(0)
    
    return digits
```

## LintCode_719 计算最大值
**描述：**
```
给一个字符串类型的数字, 写一个方法去找到最大值, 你可以在任意两个数字间加 + 或 *
```

**样例：**
```
给出 str = 01231, 返回 10 ((((0 + 1) + 2) * 3) + 1) = 10 我们得到了最大值 10
给出 str = 891, 返回 73 因为 8 * 9 * 1 = 72 和 8 * 9 + 1 = 73, 所以73是最大值
```

**Code:**
```
def calcMaxValue(self, str):
    if str is None or len(str) == 0:
        return 0
        
    nums = [int(num) for num in str]
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = max(ans + nums[i], ans * nums[i])
        
    return ans
```
