class Solution(object):
    def reverseWords(self, s):
        p=s.split()
        l=""
        for i in p[::-1]:
            l+=i+" "
        return l.strip()
        """
        :type s: str
        :rtype: str
        """
        