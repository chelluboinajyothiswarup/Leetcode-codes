class Solution(object):
    def isValid(self, s):
        l = list(s)
        if len(s)==1:
            return False
        lst = []
        for i in l:
            if i=='(':
                lst.append(i)
            if i==')':
                if len(lst)!=0 and lst[-1]== '(':
                    lst.pop()
                else:
                    return False
            if i=='[':
                lst.append(i)
            if i==']':
                if len(lst)!=0 and lst[-1]=='[':
                    lst.pop()
                else:
                    return False
            if i=='{':
                lst.append(i)
            if i=='}':
                if len(lst)!=0 and lst[-1]=='{':
                    lst.pop()
                else:
                    return False
        if len(lst)==0:
            return True
        else:
            return False

'''or'''

class Solution(object):
    def isValid(self, s):
        d = {"(":")","{":"}","[":"]"}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif  not stack or d[stack.pop()] != i:
                return False
        return not stack
