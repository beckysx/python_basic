"""
返回true or false
1. startswith(目标，开始index，结束index) 是否以目标开头
2. endswith(目标，开始index，结束index)
"""
mystr = "hello world and itcast and itheima and Python"
print(mystr.startswith('hello'))
print(mystr.startswith('hel'))
print(mystr.startswith('a'))
print(mystr.endswith('Python'))
print(mystr.endswith('on'))
print(mystr.endswith('python'))
