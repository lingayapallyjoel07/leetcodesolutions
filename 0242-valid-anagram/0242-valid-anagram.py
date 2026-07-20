class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k=sorted(s)
        l=sorted(t)
        if k==l:
            return True
        else:
            return False
            
        
        