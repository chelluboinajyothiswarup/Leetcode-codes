class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l,m = [],[]
        c=1
        for i in range(numRows):
            for j in range(0,i+1):
                if i==0 or j==0:
                    m.append(c)
                else:
                    c=(c*(i-j+1))//j
                    m.append(c)
            l.append(m)
            m = []
        return l
