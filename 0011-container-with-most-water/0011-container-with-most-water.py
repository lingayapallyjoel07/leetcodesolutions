class Solution(object):
    def maxArea(self, height):
        l=0
        m=0
        r=len(height)-1
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            a=w*h
            m=max(m,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m