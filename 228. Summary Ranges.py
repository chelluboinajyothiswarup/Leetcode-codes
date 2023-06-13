class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        s = ''
        l,m = [nums[0]],[]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                l.append(nums[i+1])
            else:
                if len(l)>1:
                    s = str(l[0])+"->"+str(l[-1])
                else:
                    s = str(l[0])
                m.append(s)
                print(l)
                l.clear()
                l.append(nums[i+1])
        if l[0]==nums[-1]:
            m.append(str(nums[-1]))
        else:
            s = str(l[0])+"->"+str(l[-1])
            m.append(s)
        return m
