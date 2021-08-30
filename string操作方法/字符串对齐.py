"""
1. str.ljust(长度，填充字符)
2. str.rjust(长度，填充字符)
3. str.center(长度，填充字符)
"""
str1 = 'hello'
print(str1.ljust(10, "!"))
print(str1.rjust(10, "!"))
print(str1.center(11, "!"))
print(str1)