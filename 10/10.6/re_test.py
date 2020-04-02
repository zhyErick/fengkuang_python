import re
# 编译得到正则表示对象
pa = re.compile('fkit')
# 调用match方法,原本应该从开始位置匹配,此处指定从索引4的地方开始匹配,可以匹配成功
print(pa.match('www.fkit.org', 4).group())

# 此处指定索引4 到索引 6之间执行匹配,匹配失败
print(pa.match('www.fkit.org', 4, 6))

# 此处指定从索引4 到索引8之间执行全匹配,匹配成功
print(pa.fullmatch('www.fkit.org', 4, 8).span())