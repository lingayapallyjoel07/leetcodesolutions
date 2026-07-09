class Solution(object):
    def addToArrayForm(self, num, k):
        l=int(''.join(map(str,num)))
        m=l+k
        p=list(map(int,str(m)))
        return p

        
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        