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
# print("my name is %s, I'm in %r, and %d years old" % ('Henry', 'HuNan', 25))
#
#
# # 定义函数def sum()相加 and palindrome()回文
# def sum(x, y):
#     return x + y
#
#
# add = sum(1, 2)
# print(add)
#
#
# def palindrome(str):
#     return str == str[::-1]
#
#
# if __name__ == '__main__':  # 作用1、__name__属性是Python的一个内置属性，被直接运行时，代码块也运行，作用2、模块导入，代码块不运行
#     str2 = input('please enter the string：')
#     if palindrome(str2):
#         print('yeah, %r is palindrome' % (str2))
#     else:
#         print('oh no, %r is not palindrome' % (str2))


# 文档字符串docstrings
# option+command+L 代码格式化
# option+shift+↕方向键 移动代码行
import math


def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side c as float
    """
    return math.sqrt(a * a + b * b)


if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(3, 4))

lst = [1, 2, 3, 4, 5]


def square(num):
    "返回所给数字的平方."
    return num * num

#高阶函数 map() 它接受一个函数和一个序列（迭代器）作为输入，
# 然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果
print(list(map(square, lst)))
