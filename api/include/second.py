
# A 和 B必须同时满足才能执行
# if '那个人是女人' and '单身':
#     print('你可以追求她')
# else:
#     print('成为基友')

#range()函数，可以生成0到x-1数
# for i in range(10):
#     print(i)

#range()函数，取某个范围区间的数，包头不包尾，尾数要+1
# for i in range(1,11):
#     print(i)

# 练习题1：书桓走后，可怜的依萍每天只能对着日记，遥寄思念。
# 现在，请你用 for 循环帮依萍写出“书桓走的第 n 天，想他”，一直写到第 10 天。
#  for i in range(1,11):
#      print('书桓走的第 {} 天，想他'.format(i))

#while循环
# a=1
# while a<5:
#     print(a)
#     a=a+1

# #练习题2：求N个数字的平均值avg=(n1+n2+n...)/n
# avg=0
# sum=0
# n=10
# count=0
# print("please input 10 number：")
# while count<n:
#     num = float(input())
#     sum=sum+num
#     count=count+1
# avg=sum/n
# print("n={},S=sum={}".format(n,sum))
# print("avg={:.2f}".format(avg))
#
# #练习题3：华氏温度到摄氏温度转换程序 C=(F-32)/1.8
# fahrenheit=0
# celsius=0
# print("please input hs number：")
# fahrenheit=float(input())
# if (fahrenheit==" "):
#     pass
# else:
#     celsius=(fahrenheit-32)/1.8
#     print("{}°F = {:.1f}°C".format(fahrenheit,celsius))

# data=("China Kongfu",10,'true')
# a,b,c=data
# print(a,b,c)

#!/usr/bin/env python3
# days = int(input("Enter days: "))
# months = days // 30
# days = days % 30
# print("Months = {} Days = {}".format(months, days))

# days = int(input("Enter days: "))
# print("Months = {} Days = {}".format(*divmod(days, 30)))

#练习4：圆的面积s=πr²
s=0
r=0
print("please input r number：")
r=float(input())
s=3.14*r*r
print("r={},s={:.2f}".format(r,s))