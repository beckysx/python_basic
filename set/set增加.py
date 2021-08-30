'''
增加内容已经有的时候，不进行任何操作
1. add() 增加单一数据
2. update() 增加序列进入集合
'''
s1 = {10, 20}

# add()
s1.add(100)
print(s1)
# s1.add([10,20,30])  # TypeError: unhashable type: 'list'

# update()
s1.update([10, 20, 30, 40, 50])
print(s1)  # {100, 40, 10, 50, 20, 30} 去重
# update只能用于序列
# s1.update(200)  # TypeError: 'int' object is not iterable
s1.update('abcd')
print(s1)
