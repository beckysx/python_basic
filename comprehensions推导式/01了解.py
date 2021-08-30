"""
用一个表达式 创建 一个有规律的列表或者 控制 一个有规律的列表
好处：化简代码
只有三种：
1. list推导式
2. dict推导式
3. set推导式
"""
list1 = [i for i in range(10)]
print(list1)

list2 = [i for i in range(10) if i % 3 == 0]  # 或者改成range(0,10,3)
print(list2)

# 多个for loop
# 需求： 创建[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
list3 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list3)
