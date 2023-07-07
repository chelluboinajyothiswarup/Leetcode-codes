class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        if len(set(s))!=len(set(t)):
            return False
        for i in range(len(t)):
            if t[i] not in d:
                d[t[i]]=s[i]
            else:
                if d[t[i]]==s[i]:
                    continue
                else:
                    return False
        return True
