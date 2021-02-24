#练习5：逢7跳过游戏
#包含取余数，倍数取模=0，十位上包含取整
# a=0
# while a < 100:
#     a=a+1
#     if(a%10==7 or a%7==0 or a//10==7):
#         continue
#     else:
#         print("逢7过：a={}".format(a))

# for a in range(1,100):
#     if (a % 10 == 7 or a % 7 == 0 or a // 10 == 7):
#         continue
#     else:
#         print("逢7过：a={}".format(a))

#遍历字典中的元素数据items()
data ={'sunny':'1','gucci':'2','lv':'3'}
# del data['lv']
'lv' in data
for x,y in data.items():
    print('{} to {}'.format(x,y))

#遍历列表或任何序列类型enumerate()
for c,d in enumerate(['English','3']):
    print(c,d)

#同时遍历多个序列类型zip()
a={'water','melon'}
b={'sub','string'}
for i,j in zip(a,b):
    print(i,j)
