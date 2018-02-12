class Solution:
    """
    @param: s: a string
    @param: p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        ans = []
        sum = [0] * 30
        plength = len(p)
        slength = len(s)
        for i in range(plength):
            sum[ord(p[i]) - ord('a')] += 1
        start = 0
        end = 0
        matched = 0
        while end < slength:
            if sum[ord(s[end]) - ord('a')] >= 1:
                matched += 1
            sum[ord(s[end]) - ord('a')] -= 1
            end += 1
            if matched == plength:
                ans.append(start)
            if end - start == plength:
                if sum[ord(s[start]) - ord('a')] >= 0:
                    matched -= 1
                sum[ord(s[start]) - ord('a')] += 1
                start += 1

        return ans

if __name__ == '__main__':
    so = Solution()
    print so.findAnagrams('abab', 'ab')