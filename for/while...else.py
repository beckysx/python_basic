"""
else 缩进代码为正常结束后执行的代码
非正常结束后不执行
"""
i = 1
while i <= 5:
    print("我错了")
    if i == 3:
        print("不真诚")
        break
    i += 1
else:
    print("好吧")


j = 1
while j <= 5:
    print("对不起")
    if j == 3:
        print("不真诚")
        j += 1
        continue
    j += 1
else:
    print("好吧")