class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    break
            if len(l)==2:
                break
        return l  
