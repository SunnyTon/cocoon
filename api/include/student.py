# 这是一个判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，
# 如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。
num = int(input('please enter the number of students ：'))
data = {}  # 存储数据字典的变量
Subjects = ('Physics', 'Math', 'history')  # 所有科目
for i in range(0, num):
    name = input('please enter the name of student {}：'.format(i + 1))
    marks = []  # 存储学生姓名
    for j in Subjects:
        marks.append(int(input('please enter marks of {}：'.format(j))))
        data[name] = marks
        for x, y in data.items():
            total = sum(y)
            print("{}'s total marks {}".format(x, total))
    if total > 120:
        print(x, 'passed')
else:
    print(x, 'failed')
