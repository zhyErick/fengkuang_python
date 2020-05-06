from pathlib import *

# 创建Purepath,实际上使用PureWindowsPath
pp = PurePath('setup.py')
print(type(pp))
pp = PurePath('crazyit', 'some/path', 'info')
print(pp)
pp = PurePath(Path('crazyit'), Path('info'))
print(pp)
pp = PurePosixPath('crazyit', 'some/path', 'info')
print(pp)
pp = PurePosixPath()
print(pp)
# 如果传入的参数包含多个根路径,则只有最后一个根路径及后面的子路径生效
pp = PurePosixPath('/etc', '/usr','lib64')
print(pp)
pp = PureWindowsPath('c:/Windows', 'd:info')
print(pp)
# 在路径中多出来的斜杠和点号(代表当前路径)都会被忽略
pp = PurePath('foo//bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)
pp = PurePath('foo/../bar')
print(pp)