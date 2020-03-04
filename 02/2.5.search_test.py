s = 'crazyit.org is a good site'
# 判断s 是否以crazyit开头
print(s.startswith('crazyit'))
# 判断s是否以site结束
print(s.endswith('site'))
# 查找s中'org'出现的位置
print(s.find('org'))
# 查找s中'org'出现的位置
print(s.index('org'))
# 从索引9处开始查找'org'出现的位置
print(s.find('org', 9))
# print(s.index('org', 9)) # 引发错误

# 将字符串中所有'it'替换成'xxxx'
print(s.replace('it','xxxx'))

# 将字符串中第一个‘it’替换为‘xxxx’
print(s.replace('it', 'xxxx', 1))

# 定义翻译映射表 97(a) -> 945(α), 98(b)->946(β), 116(t) ->964(τ)
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))