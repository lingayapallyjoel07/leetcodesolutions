class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        elif ((2**31)%n==0 and n>0) or n==1:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        