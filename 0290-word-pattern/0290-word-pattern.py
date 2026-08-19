class Solution(object):
    def wordPattern(self, pattern, s):
        l=s.split()
        d1={}
        d2={}
        for i in range(len(pattern)):
            if len(pattern)!=len(l):
                return False
            if pattern[i] in d1 and d1[pattern[i]]!=l[i]:
                return False
            if l[i] in d2 and d2[l[i]]!=pattern[i]:
                return False
            d1[pattern[i]]=l[i]
            d2[l[i]]=pattern[i]
        return True
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        