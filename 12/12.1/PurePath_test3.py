from pathlib import *
# 访问drive属性
print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('/Program Files').drive)
print(PureWindowsPath('/etc').drive)

# 访问root属性
print(PureWindowsPath('c:/Program Files/').root)
print(PureWindowsPath('c:Program Files/').root)
print(PureWindowsPath('/etc').root)

# 访问anchor属性
print(PureWindowsPath('c:/Program Files/').anchor)
print(PureWindowsPath('c:Program Files/').anchor)
print(PurePosixPath('/etc').anchor)

# 访问parents属性
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0])
print(pp.parents[1])
print(pp.parents[2])
print(pp.parents[3])

# 访问parent属性
print(pp.parent)

# 访问name属性\
print(pp.name)
pp = PurePath('abc/wawa/bb.txt')
print(pp.name)

pp = PurePath('abc/wawa/bb.txt.tar.zip')
# 访问suffixes属性
print(pp.suffixes)
print(pp.suffixes[0])
print(pp.suffixes[1])
print(pp.suffixes[2])
# 访问suffix属性
print(pp.suffix)
print(pp.stem)

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp)
# 转换成UNIX风格的路径
print(pp.as_posix())
# 将相对路径转换成URI引发异常
# print(pp.as_uri())
# 创建绝对路径
pp = PurePath('d:/', 'Python', 'Python3.6')
# 将绝对路径转换成uri
print(pp.as_uri())

# 判断当前路径是否匹配指定通配符
print(PurePath('a/b.py').match('*.py'))
print(PurePath('a/b/c.py').match('b/*.py'))
print(PurePath('a/b/c.py').match('a/*.py'))

pp = PurePosixPath('c:/abc/xyz/wawa')
# 测试relative_to方法
print(pp.relative_to('c:/'))
print(pp.relative_to('c:/abc'))
print(pp.relative_to('c:/abc/xyz'))

# 测试with_name的方法
p = PureWindowsPath('e:/Downloads/paythlib.tar.gz')
print(p.with_name('fkit.py'))
p = PureWindowsPath('e:/')
# print(p.with_name('fkit.py'))

# 测试with_suffix方法
p = PureWindowsPath('e:/Downloads/pathlib/aaa.zzz')
print(p.with_suffix('.zip'))
p = PureWindowsPath('c:/aaa/aa/')
print(p.with_suffix('.txt'))