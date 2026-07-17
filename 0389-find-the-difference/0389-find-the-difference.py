class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l=[]
        for i in t:
            l.append(i)
        for j in s:
            l.remove(j)
        return l[0]
        
        