class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                if sub==sub[::-1]:
                    if len(ans)<len(sub):
                        ans=sub
        return ans



        