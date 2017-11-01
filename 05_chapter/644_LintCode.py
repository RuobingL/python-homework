class Solution:
    """
    @param: num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        mp = {'0':'0', '1':'1', '6':'9', '8': '8', '9': '6'}
        for i in range(len(num) / 2 + 1):
            if mp.get(num[i]) != num[- i - 1]:
                return False


        return True

if __name__ == '__main__':
    mp = {'a': 1, 'b': 1}
    
