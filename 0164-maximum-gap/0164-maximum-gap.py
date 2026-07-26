class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        gap=0
        for i in range(0,len(nums)-1):
            if gap < abs(nums[i]-nums[i+1]):
                gap = abs(nums[i]-nums[i+1])
        if len(nums)<2:
            return 0
        return gap
        