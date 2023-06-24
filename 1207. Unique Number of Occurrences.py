class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        d = sorted(d.items(), key=lambda x:x[1])
        for i in range(len(d)-1):
            if d[i][1]==d[i+1][1]:
                return False
        return True
