class Solution:
    def dayOfYear(self, date: str) -> int:
        l = [31,28,31,30,31,30,31,31,30,31,30,31]
        leap = False
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        print(year,month,day)
        if((year%400==0)or(year%100!=0)and(year%4==0)):
            leap=True
        if month<=2:
            return sum(l[:month-1])+day
        if leap:
            return sum(l[:month-1])+1+day
        else:
            return sum(l[:month-1])+day
