class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1,1]
        l,m = [],[]
        c=1
        for i in range(rowIndex+1):
            for j in range(0,i+1):
                if i==0 or j==0:
                    m.append(c)
                else:
                    c=(c*(i-j+1))//j
                    m.append(c)
            l.append(m)
            m = []
        return l[-1]
