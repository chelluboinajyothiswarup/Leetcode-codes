class Solution:
    def reverse(self, x: int) -> int:
        if x>pow(2,31)-1 or x<pow(-2,31):
            return 0
        lst = [i for i in str(x)]
        print(lst)
        if lst[0]=='-':
            y=lst[1:]
            y.reverse()
            y.insert(0,'-')
            y=int(''.join(y))
            if y>pow(2,31)-1 or y<pow(-2,31):
                return 0
            else:
                return y
        else:
            lst.reverse()
            lst=int(''.join(lst))
            if lst>pow(2,31)-1 or lst<pow(-2,31):
                return 0
            else:
                return lst
