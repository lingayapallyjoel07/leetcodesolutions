class Solution(object):
    def selfDividingNumbers(self, left, right):
        p=[]
        for i in range(left,right+1):
            l=list(map(int,str(i)))
            count=0
            for k in l:
                if k==0:
                    break
                if i%k==0:
                    count+=1
            if count==len(l):
                p.append(i)
        return p



        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        