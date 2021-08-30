'''
remove() 删除指定数据，不存在就报错
discard() 删除指定数据，不存在也不报错
pop() 随机删除一个数据，并且返回这个数据
'''

s1 = {10, 20, 30, 40, 50}

# remove
s1.remove(10)
print(s1)
# s1.remove(44) # 报错KeyError: 44

# discard
s1.discard(20)
print(s1)
s1.discard(10)  # 不报错

s2 = {10, 20, 30, 40, 50}
del_num = s2.pop()
print(del_num)
