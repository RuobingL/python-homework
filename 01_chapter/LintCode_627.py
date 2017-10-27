class Solution:
    """
    @param: s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
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

if __name__ == '__main__':
    so = Solution()
    print so.longestPalindrome('aaaab')