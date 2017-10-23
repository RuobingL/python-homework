class Solution:
    """
    @param: num1: An integer
    @param: num2: An integer
    @param: num3: An integer
    @return: an interger
    """
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

