class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        c=0
        s=0
        for i in range(0,len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                f=int(str(s)[0])
                l=s%10
                if f==x and l==x:
                    c+=1
            
        return c    


        