class Solution:
    def defangIPaddr(self, address: str) -> str:
        # s=''
        # for i in address:
        #     if i=='.':
        #         s+='['+'.'+']'
        #     else:
        #         s+=i
        # return s

        # return address.replace('.','[.]')

        lst = address.split('.')
        return '[.]'.join(lst)
