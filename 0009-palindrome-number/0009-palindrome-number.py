class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        q=str(x)
        k=q[::-1]
        if y==k:
            return True
        else:
            return False
        
        