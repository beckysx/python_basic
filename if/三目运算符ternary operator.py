"""
[on_true] if [expression] else [on_false]

"""
a = 1
b = 2
c = a if a > b else b
print(c)

#  有两个变量比较大小， 如果v1>v2 则 v1-v2, 否认 v2-v1
aa = 10
bb = 16
cc = aa - bb if aa > bb else bb - aa
print(cc)
