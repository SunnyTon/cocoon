#练习5：逢7跳过游戏
#包含取余数，倍数取模=0，十位上包含取整
# a=0
# while a < 100:
#     a=a+1
#     if(a%10==7 or a%7==0 or a//10==7):
#         continue
#     else:
#         print("逢7过：a={}".format(a))

for a in range(1,100):
    if (a % 10 == 7 or a % 7 == 0 or a // 10 == 7):
        continue
    else:
        print("逢7过：a={}".format(a))

