class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            if left < right and  s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    so = Solution()
    print so.isPalindrome('A man, a plan, a canal: Panama')