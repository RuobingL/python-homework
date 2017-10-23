class Solution:
    """
    @param: character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        """
        # solution 1
        return character.upper()
        """

        # solution 2
        return chr(ord('A') - ord('a') + ord(character))

if __name__ == '__main__':
    so = Solution()
    print so.lowercaseToUppercase('a')

