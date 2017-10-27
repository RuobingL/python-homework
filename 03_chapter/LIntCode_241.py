import math
class Solution:
    """
    @param: str: A string
    @return: An integer
    """
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

if __name__ == '__main__':
    so = Solution()
    print so.stringToInteger('-123')