class Solution:
    def finalString(self, s: str) -> str:
        x = ""
        for i in s:
            if i=="i":
                x = x[::-1]
            else:
                x+=i
        return x
