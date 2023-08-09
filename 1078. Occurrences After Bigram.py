class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l = []
        lst = text.split(" ")
        for i in range(len(lst)-2):
            if lst[i]==first and lst[i+1]==second:
                l.append(lst[i+2])
        return l
