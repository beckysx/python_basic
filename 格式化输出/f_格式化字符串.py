age = 18
name = 'becky'

# 我的名字是，今年X岁
print("我的名字是%s，今年%s岁" % (name, age))

# 语法 f'{}'
print(f'我的名字是{name}，今年{age}岁')
print(f'我的名字是{name}，明年{age+1}岁')

# 效果一样 f更高效 （3.6版本之后才有）
