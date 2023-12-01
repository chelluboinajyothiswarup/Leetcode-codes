class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c = 0
        if(ruleKey=="type"):
            j = 0
        elif ruleKey=="color":
            j=1
        else:
            j=2
        for i in items:
            if i[j]==ruleValue:
                c+=1
        return c
