import re
# 正则表达式中使用组
m = re.search(r'(fkit).(org)', r'www.fkit.org is a good domain')
print(m.group(0))

# 调用的简化写法,底层是调用m.__getitem__(0)
print(m[0])
print(m.span(0))
print(m.group(1))

# 调用的简化写法,底层是调用m.__getitem__(1)
print(m[1])
print(m.span(1))
print(m.group(2))

#  调用的简化写法,底层是调用m.__getitem__(2)
print(m[2])
print(m.span(2))

# 返回所有组匹配的字符串组成的元组
print(m.group())

# 为正则表达式定义两个组,并为组指定了名字
m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)', r"www.fkit.org is a good domain")
print(m2.groupdict())

print(re.fullmatch(r'\u0041\\', 'A\\'))
print(re.fullmatch(r'\u0061\t', 'a\t'))
print(re.fullmatch(r'\?\[', '?['))


print(re.search(r'Windows (95|98|NT|2000) [\w ]+\1', 'Windows 98 published in 98'))

print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h3>'))