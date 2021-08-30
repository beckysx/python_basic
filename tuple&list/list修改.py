"""
1. 修改指定index数据
2. revers()
3. sort() reverse= Ture 降序 false 升序（默认）
"""
name_list = ['TOM', 'Lily', 'ROSE']
# 1
name_list[1] = 'LILY'
print(name_list)
# 2
list1 = [1, 3, 2, 5, 4, 9, 7]
list1.reverse()
print(list1)
# 3 sort()
list1.sort(key=None, reverse=True)  # key用于dictionary
print(list1)
