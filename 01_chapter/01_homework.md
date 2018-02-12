# 阶梯训练 Part I Variable & Control flow
## 1. LintCode_479 数组第二大数
**题目描述**:

在数组中找到第二大的数
>>  **注意事项**
>> 你可以假定至少有两个数字

**样例**:

给出 [1, 3, 2, 4], 返回 3.
给出 [1, 2], 返回 1.

这道题按照直观的理解，假如给定的list中没有重复的数，写出的程序LintCode也是AC的。

```
#solution 1
def secondMax(self, nums):
    return sorted(nums)[-2]


#solution 2
def secondMax(self, nums):
    # write your code here
    for i in range(2):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums[-2]

```
但是LintCode题目中并没有说明list是不重复的，面对[1,2,2]这样的输入，第二大的数应该是1.
```
def secondMax(self, nums):
    biggestNum = secBigNum = nums[0]

    # Get the biggest Num
    for num in nums:
        if biggestNum < num:
            biggestNum = num

    # Get the sencond big num
    for num in nums:
        if secBigNum < num and num != biggestNum:
            secBigNum = num
    return secBigNum
```

## 2. LintCode_478 简单计算器
**题目描述**
给出两个整数 a , b ,以及一个操作符 opeator
```
+, -, *, /
```
返回结果：
```
a<operator>b
```
输入样例：
```
For a = 1, b = 2, operator = +, return 3.

For a = 10, b = 20, operator = *, return 200.

For a = 3, b = 2, operator = /, return 1. (not 1.5)

For a = 10, b = 11, operator = -, return -1.
```

Python中没有switch表达式，那么只能用其它办法代替。
```
# solution 1
def calculate(self, a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b

# solution 2
def calculate(self, a, operator, b):
    res =  {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }[operator](a, b)

    return res
```


## 3. LintCode_283 三数之中的最大值

**描述：**
给三个整数，求他们中的最大值。

**样例：**
```
Given num1 = 1, num2 = 9, num3 = 0, return 9.
```


```
def maxOfThreeNumbers(self, num1, num2, num3):
    # solution 1
    res = num1
    if res < num2:
        res = num2
    if res < num3:
        res = num3
    return res

    """
    # solution 2
    return max(num1,num2,num3)
    """
```
## 4. LintCode_145 大小写转换
**描述：**
将一个字符由小写字母转换为大写字母
**样例：**
```
a -> A

b -> B
```

```
def lowercaseToUppercase(self, character):
    """
    # solution 1
    return character.upper()
    """

    # solution 2
    return chr(ord('A') - ord('a') + ord(character))
```

## 5. LintCode_37 反转一个三位整数
**描述：**
反转一个只有3位数的整数。

**样例：**
```
123 反转之后是 321。
900 反转之后是 9。
```


```
def reverseInteger(self, number):
    # solution 1
    return int(str(number)[::-1])

    """
    # solution 2
    c = number % 10
    b = number / 10 % 10
    a = number / 100

    return c * 100 + b * 10 + a
    """
```

## 6. LintCode_9 Fizz Buzz 问题
**描述：**
- 如果这个数被3整除，打印fizz.
- 如果这个数被5整除，打印buzz.
- 如果这个数能同时被3和5整除，打印fizz buzz.

**样例：**
比如 n = 15, 返回一个字符串数组：
```
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]
```


```
def fizzBuzz(self, n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('fizz buzz')
        elif i % 3 == 0:
            res.append('fizz')
        elif i % 5 == 0:
            res.append('buzz')
        else:
            res.append(str(i))

    return res
```

## 7. LintCode_449 字符串转整数
**描述：**
```
将字符转换为一个整数。你可以假设字符是ASCII码，也就是说转换后的整数在0~255之间。
```

**样例:**
```
给出 a, 返回 97。
给出 %, 返回 37。
```

**Code:**
```
def charToInteger(self, character):
    # write your code here
    return ord(character)
```

## 8. LintCode_146 大小写转换II
**描述：**
```
将一个字符串中的小写字母转换为大写字母。忽略其他不是字母的字符。
```

**样例：**
```
给出 "abc", 返回 "ABC".

给出 "aBc", 返回 "ABC".

给出 "abC12", 返回 "ABC12".
```

**Code:**
```
def lowercaseToUppercase2(self, str):
    return str.upper()
```

## 9. LintCode_627 最长回文串
**描述：**
```
给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。

数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。
```

**样例：**
```
给出 s = "abccccdd" 返回 7

一种可以构建出来的最长回文串方案是 "dccaccd"。
```

**Code：**
```
def longestPalindrome(self, s):
    if s == '':
        return 0

    count_dict = {}
    for item in s:
        if item not in count_dict:
            count_dict[item] = True
        else:
            del count_dict[item]

    if len(count_dict) > 0:
        return len(s) - len(count_dict) + 1
    else:
        return len(s) - len(count_dict)
```
