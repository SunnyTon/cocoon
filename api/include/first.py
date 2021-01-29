#定义变量
level=1
HP=100
ATK=5

#打印单行文本
print('hello world')

#打印多行文本
print('''....床前明月光，
....疑是地上霜。
....举头望明月，
....低头思故乡。''')

age=input('请输入你的年龄')
print(age)
name=input('请输入你的姓名')
#{}占位符，串联行，使用format()实现插入效果，代替传统的"+"
print("你的姓名{},你的年龄{}".format(name,age))

#保留2位小数位数，format()格式化函数
print("{:.2F}".format(3.1415926))

