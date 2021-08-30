"""
1. del 删除整个variable
2. pop(index) 删除指定位置，不写index默认删除最后一个数据
3. remove(内容) 删除指定内容第一个匹配项
3. clear() 清空数据成为空列表
"""
name_list = ['TOM', 'Lily', 'ROSE']
#del name_list
del name_list[0]
print(name_list)

# 2 pop删除指定位置，不写index默认删除最后一个数据 返回被删除的数据
name_list2 = ['TOM', 'Lily', 'ROSE']
del_name= name_list2.pop()
print(del_name)
print(name_list2)
# 3 删除指定内容第一个匹配项
name_list3 = ['TOM', 'Lily', 'ROSE']
name_list3.remove("TOM")
print(name_list3)
# 4 清空数据成为空列表
name_list3.clear()
print(name_list3)