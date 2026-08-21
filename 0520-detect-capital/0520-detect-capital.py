class Solution(object):
    def detectCapitalUse(self, word):
        w=word.upper()
        l=word.lower()
        k=word.capitalize()
        if w==word or l==word or k==word:
            return True
        return False
        """
        :type word: str
        :rtype: bool
        """
        