class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cm=0
        k=set(nums)
        for i in k:
           if nums.count(i)>cm:
            cm=nums.count(i)
            m=i
        return m
           
            

        