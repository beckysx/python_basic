'''
快速合并列表成为dict，或提取目标数据
'''
# 1 创建一个dict，key是1～5，value是二次方
dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)

list1 = ['name', 'age', 'gender']
list2 = ['Tom', '20', 'male']
dict2 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict2)

# 提取信息
counts = {'mac': 100, 'mbp': 230, 'lenovo': 199, 'acer': 99, 'dell': 202}
count = {key: value for key, value in counts.items() if value >= 200}
print(count)
