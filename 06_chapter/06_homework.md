# 阶梯训练 6 - Tree & Recursion
## LintCode_366 斐波那契数列
**描述：**
```
查找斐波纳契数列中第 N 个数。

所谓的斐波纳契数列是指：
    前2个数是 0 和 1 。
    第 i 个数是第 i-1 个数和第i-2 个数的和。
斐波纳契数列的前10个数字是：

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
```

**样例：**
```
给定 1，返回 0

给定 2，返回 1

给定 10，返回 34
```

**Code：**
```
def fibonacci(self, n):
    # solution 1
    cur, a, b = 0, 0, 1
    nums = [0, 1]

    if n == 1:
        return 0
    if n == 2:
        return 1

    for i in range(2, n):
        nums.append(nums[-1] + nums[-2])
    return nums[-1]



    # # solution 2
    # a, b = 0, 1
    # for i in range(0, n - 1):
    #     a, b = b, a + b
    # return b
```

## LintCode_376 二叉树的路径和
**描述：**
```
给定一个二叉树，找出所有路径中各节点相加总和等于给定 目标值 的路径。

一个有效的路径，指的是从根节点到叶节点的路径。
```

**样例：**
```
给定一个二叉树，和 目标值 = 5:

     1
    / \
   2   4
  / \
 2   3

返回：

[
  [1, 2, 2],
  [1, 4]
]
```

**Code:**
```
def binaryTreePathSum(self, root, target):
    result = []
    path = []
    self.dfs(root, path, result, 0, target)

    return result

def dfs(self, root, path, result, len, target):
    if root == None:
        return

    path.append(root.val)
    len += root.val

    if root.left is None and root.right is None and len == target:
        result.append(path[:])

    self.dfs(root.left, path, result, len, target)
    self.dfs(root.right, path, result, len, target)

    path.pop()

```


## LintCode_482 二叉树的某层结点之和
**描述：**
```
计算二叉树的某层节点之和。
```

**样例：**
```
     1
   /   \
  2     3
 / \   / \
4   5 6   7
   /       \
  8         9
如果给出 depth = 2, 和为 5。
如果给出 depth = 3, 和为 22。
如果给出 depth = 4, 和为 17。
```

**Code:**
```
def levelSum(self, root, level):
    if root is None or level == 0:
        return 0

    ans = []
    queue = []
    queue.append(root)
    while len(queue) != 0:
        one_level = []
        # node = TreeNode()
        length = len(queue)

        for i in range(length):
            node = queue.pop(0)
            one_level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        ans.append(one_level[:])

    if level > len(ans):
        return 0
    return sum(ans[level - 1])
```

## LintCOde_481 二叉树的所有路径
**描述：**
```
计算二叉树的叶子节点之和
```

**样例：**
```
    1
   / \
  2   3
 /
4
```

**Code:**
```
# def leafSum(self, root):
#     if root is None:
#         return 0
#     ans = []
#     self.dfs(root, ans)
#     return sum(ans)

# def dfs(self, root, ans):
#     if root is None:
#         return

#     if root.left is None and root.right is None:
#         ans.append(root.val)

#     self.dfs(root.left, ans)
#     self.dfs(root.right, ans)

def leafSum(self, root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val

    return self.leafSum(root.left) + self.leafSum(root.right)
```

## LintCode_480 二叉树的所有路径
**描述：**
```
给一棵二叉树，找出从根节点到叶子节点的所有路径。
```

**样例：**
```
给出下面这棵二叉树：

   1
 /   \
2     3
 \
  5
所有根到叶子的路径为：

[
  "1->2->5",
  "1->3"
]
```

**Code:**
```
def binaryTreePaths(self, root):
    ans = []
    res = []
    if root is None:
        return ans

    self.dfs(root, ans, [])

    for list in ans:
        res.append('->'.join([str(i) for i in list]))

    return res

def dfs(self, root, ans, path):
    if root is None:
        return

    path.append(root.val)

    if root.left is None and root.right is None:
        ans.append(path[:])

    self.dfs(root.left, ans, path)
    self.dfs(root.right, ans, path)

    path.pop()
```

## LintCode_97 二叉树的最大深度
**描述：**
```
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。
```

**样例：**
```
给出一棵如下的二叉树:

  1
 / \
2   3
   / \
  4   5

这个二叉树的最大深度为3.
```

**Code:**
```
def maxDepth(self, root):
    depth = 0
    if root is None:
        return depth

    return max(self.dfs(root.left, depth + 1), self.dfs(root.right, depth + 1))

```

## LintCode_68 二叉树的后序遍历
**描述：**
```
给出一棵二叉树，返回其节点值的后序遍历。
```

**样例：**
```
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [3,2,1]
```

**Code:**
```
ans = []
def postorderTraversal(self, root):
    if root is None:
        return []

    self.postorderTraversal(root.left)
    self.postorderTraversal(root.right)
    self.ans.append(root.val)

    return self.ans
```

## LintCode_67 二叉树的中序遍历
**描述：**
```
给出一棵二叉树,返回其中序遍历
```

**样例：**
```
给出二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [1,3,2].
```

**Code:**
```
ans = []

def inorderTraversal(self, root):
    if root is None:
        return []

    self.inorderTraversal(root.left)
    self.ans.append(root.val)
    self.inorderTraversal(root.right)

    return self.ans
```

## LintCode_66 二叉树的前序遍历
**描述：**
```
给出一棵二叉树，返回其节点值的前序遍历。
```

**样例：**
```
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
 返回 [1,2,3].
```

**Code:**
```
ans = []

def preorderTraversal(self, root):
    if root is None:
        return []

    self.ans.append(root.val)
    self.preorderTraversal(root.left)
    self.preorderTraversal(root.right)

    return self.ans
```
