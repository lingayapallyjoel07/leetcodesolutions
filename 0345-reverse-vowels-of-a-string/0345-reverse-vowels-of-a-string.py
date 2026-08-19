class Solution(object):
    
    def reverseVowels(self, s):
        vow="aeiouAEIOU"
        vow1=[]
        ind=[]
        for i in range(len(s)):
            if s[i] in vow:
                vow1.append(s[i])
                ind.append(i)
        
        l=list(s)
        for i in ind:
            l[i]=vow1[-1]
            vow1.pop(-1)
        s="".join(l)
        return s





        """
        :type s: str
        :rtype: str
        """
        