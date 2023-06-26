class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i]==1 and y==0:
                y+=1
            elif nums[i]==1 and y!=0:
                if x>=k:
                    x = 0
                    continue
                else:
                    return False
            else:
                x+=1
        return True
