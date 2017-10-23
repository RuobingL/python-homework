import sys
class Solution:
    """
    @param: : An integer array
    @return: The second max number in the array.
    """

    """
    solution 2

    def secondMax(self, nums):
        return sorted(nums)[-2]

    """

    """
    solution 1

    def secondMax(self, nums):
        # write your code here
        for i in range(2):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[-2]
    """

    # solution 3
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

if __name__ == '__main__':
    so = Solution()
    print so.secondMax([1,2,2])

