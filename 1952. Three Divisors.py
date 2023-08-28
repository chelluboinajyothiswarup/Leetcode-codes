class Solution:
    def isThree(self, n: int) -> bool:
        x = 1
        for i in range(1,n//2+1):
            if n%i==0:
                x+=1
            if x>3:
                return False
        if x<3:
            return False
        return True
