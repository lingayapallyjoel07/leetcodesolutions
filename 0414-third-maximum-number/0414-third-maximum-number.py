class Solution(object):
    def thirdMax(self, nums):
        set(nums)
        l=list(set(nums))
        l.sort()
        l.reverse()
        if len(l)>=3:
            return l[2]
        elif len(l)==2:
            return l[0]
        else:
            return l[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        