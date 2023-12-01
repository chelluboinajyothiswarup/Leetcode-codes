class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s = ""
        y = ""
        for i in word1:
            s+=i
        for i in word2:
            y+=i
        return s==y
