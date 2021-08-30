"""
int(x)        x-> int
eval(str)            计算字符串中有效python表达式，并返回一个对象
tuple(s)
list(s)
float(x)
str(x)
"""
# eval()
str1 = '1'
str2 = '1.1'
str3 = '(1,2,3)'
str4 = '[1,2,3]'
str5 = str(["3","4","5"])
x =eval(str5)
print(type(x[2]))