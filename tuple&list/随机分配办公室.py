import random

'''
八个老师随机分配到三个办公室
1 准备数据
    老师--列表
    办公室--列表嵌套
2 分配老师到办公室
    随机分配
    名字写入办公室
3 验证
'''
teacher = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
offices = [[], [], []]
for t in teacher:
    officenum = random.randint(0, 2)
    offices[officenum].append(t)
for office in offices:
    print(f'办公室{offices.index(office) + 1}有{len(office)}人,分别是： ', end='')
    for t in office:
        print(t, end=" ")
    print()
