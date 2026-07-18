class Solution:
    def arrangeCoins(self, n: int) -> int:
        p=n
        for i in range(1,n+1):
            p-=i
            if p==0:
                return i
            elif p<0:
                return i-1
        