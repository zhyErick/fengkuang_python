from collections import Counter
# 创建Counter对象
cnt = Counter()
# 访问并不存在的key,将该输出的key次数为0
print(cnt['Python'])
for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
    cnt[word] += 1
print(cnt)
# 只访问Counter对象元素
print(list(cnt.elements()))

# 将字符串(迭代器)转换成Counter
chr_cnt = Counter('abracadabra')
# 获取出现最多的三个字母
print(chr_cnt.most_common(3))
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
# 用Counter对象执行减法,其实就是减少各元素出现的次数
c.subtract(d)
print(c)
e = Counter({'x': 2, 'y': 3, 'z': -4})
# 用del删除key-value对,会真正删除key-value对
del e['y']
print(e)