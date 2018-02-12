# 阶梯训练 第五章课后作业 树结构与递归 Tree & Recursion
## 1. LIntCode_647 子串之谜
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

**Code:**
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

## 2. LintCode_664 镜像数字
**描述：**
```
一个镜像数字是指一个数字旋转180度以后和原来一样(倒着看)。
写下一个函数来判断是否这个数字是镜像的。数字用字符串来表示。
```

**样例：**
```
例如，数字"69"，"88"，和"818"都是镜像数字。
给出数字 num = "69"
返回 true
给出数字 num = "68"
返回 false
```

**Code：**
```
def isStrobogrammatic(self, num):
    mp = {'0':'0', '1':'1', '6':'9', '8': '8', '9': '6'}
    for i in range(len(num) / 2 + 1):
        if mp.get(num[i]) != num[- i - 1]:
            return False
    return True
```

## 3. LintCode_557 字符统计
**描述：**
```
对一个字符串中的字符进行计数, 返回一个hashmap, key为字符, value是这个字符出现的次数.
```

**样例：**
```
给出 str = "abca", 返回

{
  "a": 2,
  "b": 1,
  "c": 1
}
```

**Code:**
```
def countCharacters(self, str):
    mp = {}
    for c in str:
        if not mp.has_key(c):
            mp[c] = 1
        else:
            mp[c] += 1
    return mp
```

## 4. LintCode_487 姓名去重
**描述：**
```
给一串名字，将他们去重之后返回。两个名字重复是说在忽略大小写的情况下是一样的。
```

**样例：**
```
给出：

[
  "James",
  "james",
  "Bill Gates",
  "bill Gates",
  "Hello World",
  "HELLO WORLD",
  "Helloworld"
]
返回：

[
  "james",
  "bill gates",
  "hello world",
  "helloworld"
]
返回名字必须都是小写字母。
```

**Code:**
```
def nameDeduplication(self, names):
    names = [name.lower() for name in names]
    mp = {}
    res = []
    for name in names:
        if not mp.has_key(name):
            mp[name] = 1
            res.append(name)
        else:
            continue
    return res
```


