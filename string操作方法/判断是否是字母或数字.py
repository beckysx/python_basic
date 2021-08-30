"""
1. isalpha() 全部是字母返回true
2. isdigit() 全部是数字返回true
3. isalnum() 至少有一个字符 且 全部字符是 字母 或者数字 或者字母数字混合 返回true
4. isspace() 字符串只包含空白返回true
"""
str1 = "123456"
str2 = "hello123456"
str3 = "hello"
str4 = "      "
mystr = "hello world and itcast and itheima and Python"

print(mystr.isalpha())   # false 含有空白
print(str1.isdigit())    # true
print(str2.isdigit())   # false 有字母
print(str2.isalpha())   # false 有数字
print(str3.isalpha())   # true

print(str1.isalnum())   # true
print(str2.isalnum())   # true
print(str3.isalnum())   # true
print(mystr.isalnum())   # false 有空格

print(str4.isspace())

