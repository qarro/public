#-*-coding:utf-8-*-
year = int(input("输入年份"))
if(year%4==0 and year%100!=0)or year%400==0:
    print(year,"年是闰年")
else:
    print(year,"不是闰年")