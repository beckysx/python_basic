"""
查找：查找位置，查找次数
1. str.find(目标，开始index，结束index) 后两个parameter不写则搜索全文
    返回目标开始位置index，目标不存在返回-1
   str.rfind(目标，开始index，结束index) 查找从右侧开始

2. str.index(目标，开始index，结束index)
    str.rindex(目标，开始index，结束index) 查找从右侧开始
    返回目标开始位置index，目标不存在报异常

3. 返回目标出现次数
"""
mystr = "hello world and itcast and itheima and Python"
my2 = 'hello'
# 1. find()
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # -1 目标不存在
print(my2.rfind('l'))  # 3

# 2. index()
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
#print(mystr.index('ands'))  # 报错

# 3. count()
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('and'))     # 3
print(mystr.count('ands'))    # 0
