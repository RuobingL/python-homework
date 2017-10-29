class Solution:
    """
    @param: s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        res = ['#']
        for item in s:
            if res[-1] == '(' and item == ')':
                res.pop()
            elif res[-1] == '{' and item == '}':
                res.pop()
            elif res[-1] == '[' and item == ']':
                res.pop()
            else:
                res.append(item)

        if len(res) == 1:
            return True
        else:
            return False