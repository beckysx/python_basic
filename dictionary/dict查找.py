'''
1 key查找
2 函数
    dict_name.get(key,默认值) key不存在返回默认，没有默认值返回None
    keys() 获取所有key 返回type：dict_keys 可迭代对象
    values() 获取所有value 返回type：dict_values 可迭代对象
    items() 获取所有key-value对，返回type：dict_items 可迭代对象，由tuple组成
'''
dict1 = {'name': 'TOM', 'age': 20, 'gender': 'male'}
print(dict1['name'])  # Tom
# print(dict1['id'])  # 报错

# 2 functions
# 2.1 get()
print(dict1.get('name'))  # TOM
print(dict1.get('names'))  # None
print(dict1.get('names', 'lily'))  # lily

# 2.2 keys()
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])
print(type(dict1.keys()))  # dict_keys 可迭代对象

# 2.3 values()
print(dict1.values())  # dict_values(['TOM', 20, 'male'])
print(type(dict1.values()))  # dict_values 可迭代对象

# 2.4 items()
print(dict1.items())  # dict_items([('name', 'TOM'), ('age', 20), ('gender', 'male')])
print(type(dict1.items()))  # dict_items 可迭代对象
