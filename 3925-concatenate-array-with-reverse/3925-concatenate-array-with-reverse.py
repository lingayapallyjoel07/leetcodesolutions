class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        l=nums[:]
        for i in nums[::-1]:
            l.append(i)
        return l
        