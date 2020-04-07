import re
# 返回所有匹配pattern的子串的组成列表,忽略大小写
print(re.findall('fkit', 'Fkit is very good, Fkit.org is my favorite', re.I))
# 返回所有匹配pattern的子串组成的迭代器,忽略大小写
it = re.finditer('fkit', 'FkIt is very good, Fkit.org is my favorite', re.I)
for e in it:
    print(str(e.span()) + "-->" + e.group())