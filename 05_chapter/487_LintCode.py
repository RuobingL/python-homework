class Solution:
    """
    @param: names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        names = [name.lower() for name in names]
        mp = {}
        res = []
        for name in names:
            if not mp.has_key(name):
                mp[name] = 1
                res.append(name)
            else:
                continue
        return res
