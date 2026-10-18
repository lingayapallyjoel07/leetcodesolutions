class Solution(object):
    def backspaceCompare(self, s, t):
        stacks=[]
        stackt=[]
        for i in s:
            if i=="#":
                if len(stacks)==0:
                    continue
                stacks.pop()
            else:
                stacks.append(i)
        for i in t:
            if i=="#":
                if len(stackt)==0:
                    continue
                stackt.pop()
            else:
                stackt.append(i)
        if stacks==stackt:
            return True
        return False       


        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        