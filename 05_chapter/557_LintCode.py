class Solution:

    def countCharacters(self, str):
        mp = {}
        for c in str:
            if not mp.has_key(c):
                mp[c] = 1
            else:
                mp[c] += 1
        return mp


if __name__ == '__main__':
    so = Solution()

    print so.countCharacters('abca')
