#!/usr/bin/python
#-*-coding:UTF-8 -*-
#：输入某年某月某日，判断这一天是这一年的第几天？
year = int(input('年：\n'))
month = int(input('月：\n'))
day = int(input('日：\n'))

a = (0,31,59,90,120,151,181,212,273,304,334)
if 0<month<2 and day<32:
    x = a(month-2)+day


