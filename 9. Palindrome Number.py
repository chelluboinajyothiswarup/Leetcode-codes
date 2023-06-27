class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        temp=x[::-1]
        if x==temp and int(x)>=0:
            return True
        else:
            return False
