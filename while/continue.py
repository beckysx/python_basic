# 吃五个苹果 吃到第三个有虫，第三个不吃了，但要继续吃第四个第五个
# 只有第三个不吃
i = 1
while i <= 5:
    if i == 3:
        print('有虫')
        i += 1
        continue  # 如果使用continue，要在continue之前修改accumulator，否则陷入死循环
    print(f'吃了{i}个苹果')
    i += 1
