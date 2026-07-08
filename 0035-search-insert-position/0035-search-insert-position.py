class Solution(object):
    def searchInsert(self, nums, target):
        nums.append(target)
        nums.sort()
        return nums.index(target)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        