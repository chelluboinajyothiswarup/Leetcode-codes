class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        m = 0
        for i in s:
            if i=='R':
                l+=1
            else:
                l-=1
            if l==0:
                m+=1
                l=0
        return m
