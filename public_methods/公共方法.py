'''
len()
del / del()
max()
min()
range(start, end, step) 生成从start到end的数字，for loop使用
enumerate(对象name,start = 0)更改index 将一个可遍历的对象组合为一个索引序列，同时列出index和对应数据，用于for loop
'''
print(range(1, 10))  # 一个可迭代对象，必须配合loop才能拿到数字

for i in range(1, 10, 2):  # 不含结束
    print(i)

for i in range(10):  # 不含结束，0～9，不写开始默认从0开始
    print(i)

list1 = ['a', 'b', 'c', 'd']
for i in enumerate(list1): # 返回tuple
    print(i)
for i in enumerate(list1,start=1): # 返回tuple, index从1开始
    print(i)