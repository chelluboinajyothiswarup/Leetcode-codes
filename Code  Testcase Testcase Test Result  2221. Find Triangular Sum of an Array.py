class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while(1<len(nums)):
            l=[]
            for i in range(len(nums)-1):
                l.append((nums[i] + nums[i+1]) % 10)
            nums = l
        return nums[0]
