class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        x = len(a)
        y = len(b)
        if a==b:
            return -1
        return max(x,y)
