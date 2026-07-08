class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        sum=0
        for i in range(0,n+k+1):
            if abs(n-i)<=k and n&i==0:
                sum+=i
        return sum
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        