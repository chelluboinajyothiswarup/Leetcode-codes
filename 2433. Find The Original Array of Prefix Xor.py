class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        x = []
        x.append(pref[0])
        for i in range(len(pref)-1):
            x.append(pref[i]^pref[i+1])
        return x
