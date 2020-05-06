from pathlib import *
import fnmatch

# 遍历当前目录下的所有文件和子目录
for file in Path('.').iterdir():
    # 访问所有以_test.py结尾的文件
    if fnmatch.fnmatch(file, '*_test.py'):
        print(file)

names = ['a.py', 'b.py', 'c.py', 'd.py']
# 对names列表进行过滤
sub = fnmatch.filter(names, '[ac].py')
print(sub)

print(fnmatch.translate('?.py'))
print(fnmatch.translate('[ac].py'))
print(fnmatch.translate('[a-c].py'))