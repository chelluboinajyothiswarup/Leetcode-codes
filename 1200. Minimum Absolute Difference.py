class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        x = float("inf")
        l = []
        z = len(arr)-1
        for i in range(z):
            y = arr[i+1]-arr[i]
            if y<x:
                x = y
        for i in range(z):
            if arr[i+1]-arr[i]==x:
                l.append([arr[i],arr[i+1]])
        return l
