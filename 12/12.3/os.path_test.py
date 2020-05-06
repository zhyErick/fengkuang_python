from pathlib import *
import fnmatch

# 遍历当前目录下的所有文件和子目录
for file in Path('../').iterdir():
    # 访问所有以_test.py结尾的文件
    print(file)
    if fnmatch.fnmatch(file, '*_test.py'):
        print(file)