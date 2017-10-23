# 第一次课的作业
## 1. LintCode_479 数组第二大数
**题目描述**:

在数组中找到第二大的数
>>  注意事项
>> 你可以假定至少有两个数字

**样例**:

给出 [1, 3, 2, 4], 返回 3.
给出 [1, 2], 返回 1.

这道题安按照直观的理解，假如给定的list中没有重复的数，写出的程序LintCode也是AC的。

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


## 3. LintCode_283 三数之中的最大值

## 4. LintCode_145 大小写转换

## 5. LintCode_FIZZ Buzz 问题