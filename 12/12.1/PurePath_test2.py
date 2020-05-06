from pathlib import *

# 比较2个Unix风格的路径,区分大小写
print(PurePosixPath('info') == PurePosixPath('INFO'))
# 比较2个Windows风格的路径,不区分大小写
print(PureWindowsPath('info') == PureWindowsPath('INFO'))
# Windows风格的路径不区分大小写
print(PureWindowsPath('INFO') in {PureWindowsPath('info')})
# UNIX风格的路径区分大小写,所以"D:" 小于 "c:"
print(PurePosixPath('D:') < PurePosixPath('c:'))
# Windows风格的路径不区分大小写,所以"d:"("D:") 大于'C'
print(PureWindowsPath('D:') > PureWindowsPath('c:'))
# 不同风格的路径可以判断是否相等(总不相等)
print(PureWindowsPath('crazyit') == PurePosixPath('crazyit'))
# 不同风格的路径不能判断大小,否则会引发错误
# print(PureWindowsPath('info') < PurePosixPath('info'))
pp = PureWindowsPath('abc')
# 将多个路径连接起来(Windows风格的路径)
print(pp/'xyz'/'wawa')
pp = PurePosixPath('abc')
print(pp/'xyz'/'wawa')
pp2 = PurePosixPath('haha','hehe')
print(pp/pp2)

pp = PureWindowsPath('abc', 'xyz', 'wawa')
print(str(pp))
pp = PurePosixPath('abc', 'xyz', 'wawa')
print(str(pp))