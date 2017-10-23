class Solution:
    """
    @param: number: A 3-digit number.
    @return: Reversed number.
    """
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