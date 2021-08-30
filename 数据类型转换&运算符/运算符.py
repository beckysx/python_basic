"""
1. 算数运算符 arithmetic operator
    1.1 / 除
    1.2 // 整除 floor division
    1.3 % modulus

2. comparison operator

3. logical operator
    and or not

4. assignment operator 复合赋值
    = += -= *=

5. bitwise operator & |
    Bitwise operators act on operands as if they were
    strings of binary digits. They operate bit by bit,
    hence the name.

"""

# 多变量赋值
num1, str1, float2 = 1, "hello", 1.1
a = b = 1


c = 10
c += 1 + 2
# c = 10+1+2 ?
# c += 3 ?         先计算预算符右面表达式
d = 10
d *= 1 + 2
print(d)  # d = 30 d= 10 * (1+2)

num1 = 0
num2 = 1
num3 = 2
# and 一个值为0，结果为0，否则为最后一个非0数字
print(num1 and num2)  # 0
print(num2 and num1)  # 0
print(num2 and num3)  # 2
# or 所有值为0才输出0，否则结果为第一个非0数字
print(num2 or num1)  # 1
print(num1 or num2)  # 1
print(num2 or num3)  # 1

