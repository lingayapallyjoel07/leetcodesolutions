class Solution(object):
    def findRestaurant(self, list1, list2):
        d={}
        l=[]
        for i in list1:
            if i in list2:
                d[i]=list1.index(i)+list2.index(i)
        for i in d:
            if min(d.values())==d[i]:
                l.append(i)
        return l
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        