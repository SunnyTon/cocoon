# 这是一个判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，
# 如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。
# num = int(input('please enter the number of students ：'))
# data = {}  # 存储数据字典的变量
# Subjects = ('Physics', 'Math', 'History')  # 所有科目
# for i in range(0, num):
#     name = input('please enter the name of student {}：'.format(i + 1))
#     marks = []  # 存储学生信息
#     for j in Subjects:
#         marks.append(int(input('please enter marks of {}：'.format(j))))
#         data[name] = marks
#         for x, y in data.items():
#             total = sum(y)
#             print("{}'s total marks {}".format(x, total))
#     if total > 120:
#         print(x, 'passed')
# else:
#     print(x, 'failed')

# 字符串%s %r %d十进制整数 %f浮点型 %%字符%
print("my name is %s, I'm in %r, and %d years old" % ('Henry', 'HuNan', 25))


# 定义函数def sum()相加 and palindrome()回文
def sum(x, y):
    return x + y


add = sum(1, 2)
print(add)


def palindrome(str):
    return str == str[::-1]


if __name__ == '__main__':  # 作用1、__name__属性是Python的一个内置属性，被直接运行时，代码块也运行，作用2、模块导入，代码块不运行
    str2 = input('please enter the string：')
    if palindrome(str2):
        print('yeah, %r is palindrome' % (str2))
    else:
        print('oh no, %r is not palindrome' % (str2))
