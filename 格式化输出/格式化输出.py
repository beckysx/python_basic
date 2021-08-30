"""
%s 字符串
%d 有符号的十进制整数
%f 浮点数
1. 准备数据
2. 使用格式化符号输出
"""
age = 18
name = 'becky'
weight = 75.5
stu_id = 1
stu_id2 = 1000

# 我今年年龄是X岁
print("我今年年龄是%d岁" % age)

# 我体重是X公斤
print("我体重是%f公斤" % weight)
print("我体重是%.2f公斤" % weight)  # keep 2 decimal

# 我的学号是X
print("我的学号是% d" % stu_id)
# 我的学号是001 不足三位数以0补全，超出三位数原样输出
print("我的学号是%03d" % stu_id)
print("我的学号是%03d" % stu_id2)

# 我的名字是，今年X岁 按顺序填入variable name
print("我的名字是%s，今年%d岁" % (name, age))
print("我的名字是%s，明年%d岁" % (name, age+1))

