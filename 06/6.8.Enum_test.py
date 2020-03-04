import enum
# 定义season枚举类
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))

# 直接访问指定枚举
print(Season.SPRING)

# 直接访问枚举类成员的变量名
print(Season.SPRING.name)

# 访问枚举成员的值
print(Season.SPRING.value)

# 根据枚举变量名访问枚举对象
print(Season['SUMMER'])

# 根据枚举值访问枚举对象
print(Season(3))

# 遍历Season枚举的所有成员
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)