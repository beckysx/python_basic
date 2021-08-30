"""
1. list.append(数据)
2. extend extend序列，拆开后放入list，包括string都会拆成字母
3. insert 指定位置，不拆开新增序列，同append
"""
name_list = ['TOM', 'Lily', 'ROSE']
name_list.append("xiaoming")
# 如果append的是一个序列，则append整个序列
name_list.append([11,22])
print(name_list)

name_list2 = ['TOM', 'Lily', 'ROSE']
name_list2.extend("xiaoming")
name_list2.extend([11,22])
print(name_list2)

name_list3 = ['TOM', 'Lily', 'ROSE']
name_list3.insert(1,['aaa','bbb'])
print(name_list3)
