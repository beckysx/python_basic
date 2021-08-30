'''
创建使用{}或者set()，但是空集合只能使用set(),否则创建的是dict
集合中的数据不允许重复！！
不能使用index，不按输入顺序排列
'''

# 1. 创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)  # {50, 20, 40, 10, 30}

s2 = {10, 20, 30, 30, 40, 50}
print(s2)  # {50, 20, 40, 10, 30}

s3 = set('abcdefg')
print(s3)  # {'g', 'd', 'b', 'a', 'c', 'e', 'f'}

# 2. 创建空集合: set()
s4 = set()
print(s4)
print(type(s4))  # set
s5 = {}
print(type(s5))  # dict
