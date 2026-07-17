class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            p=-1*x
        else:
            p=x
        k=0
        while p>0:
            n=p%10
            k=k*10+n
            p=p//10
        if k<-2**31 or k>2**31-1:
            return 0
        elif x<0:
            return -1*k
        else:
            return k

        