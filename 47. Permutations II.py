from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst = []
        for i in permutations(nums):
            if list(i) not in lst:
                lst.append(list(i))
        return lst
