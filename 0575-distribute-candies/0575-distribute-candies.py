class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        p=set(candyType)
        p1=len(p)
        l=len(candyType)
        c=l//2
        if c>=p1:
            return p1
        else:
            return c