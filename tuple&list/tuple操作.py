"""
不支持修改，只支持查找
tuple.index(数据)
tuple.count(数据)
len(tuple)

tuple内数据直接修改会报错，但是可以修改tuple内list中的数据
"""
t = ('aa', 'bb', ['cc', 'dd'])
t[2][0] = 'cccccc'
print(t)
