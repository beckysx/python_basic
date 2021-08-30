age = int(input("type your age: "))

if age < 18:
    print(f'your age is {age}, to young')
elif 18 <= age <= 60:  # 简化写法 ((age>=18) and (age<=60))
    print(f'your age is {age}, ok')
elif age > 60:
    print(f'your age is {age}, too old')