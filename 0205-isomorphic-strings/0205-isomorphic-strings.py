class Solution(object):
    def isIsomorphic(self, s, t):
        d={}
        d1={}
        for i in range(len(s)):
            if s[i] in d and d[s[i]]!=t[i]:
                return False
            if t[i] in d1 and d1[t[i]]!=s[i]:
                return False
            d[s[i]]=t[i]
            d1[t[i]]=s[i]
        return True
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        