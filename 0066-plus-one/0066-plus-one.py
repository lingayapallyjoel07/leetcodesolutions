class Solution(object):
    def plusOne(self, digits):
        x=int(''.join(map(str,digits)))
        p=x+1
        lst=[int(i) for i in str(p)]
        return lst
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        