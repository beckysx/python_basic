"""
break 终止次循环
continue 退出当前 一次 循环， 进入下一个循环
"""
# 循环吃五个苹果 吃完第三个之后不吃了 ==4 或者 >3
i = 0
while i < 5:
    if i >= 3:
        print('吃饱了')
        break
    print(f'吃了{i+1}个苹果')
    i+=1