# 增 dic_name[key]=value 不存在则增加key-value，存在key则修改原value
dict1 = {'name': 'TOM', 'age': 20, 'gender': 'male'}
dict1['id'] = 110
dict1['name'] = 'ROSE'
print(dict1)

# 删 del clear
dict2 = {'name': 'TOM', 'age': 20, 'gender': 'male'}
del dict2['name']
print(dict2)
dict2.clear()
print(dict2)