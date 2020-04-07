import re
# 使用逗号对字符串进行分割
print(re.split(', ', 'fkit, fkjava, crazyit'))

# 指定只分割一次,被切成两个子串
print(re.split(', ', 'fkit, fkjava, crazyit', 1))

# 使用a进行分割
print(re.split('a', 'fkit, fkjava, crazyit'))