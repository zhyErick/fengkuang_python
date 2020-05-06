from pathlib import *

# 获取当前目录
p = Path('../')

# 遍历当前目录下的所有文件和子目录
for x in p.iterdir():
    print(x)

# 获取上一级目录
p = Path('../')
# 获取上级目录及其所有子目录的.py文件
for x in p.glob('**/*.py'):
    print(x)

# 获取C:\python\oldboy_python对应的目录
p = Path('C:\python\oldboy_python')
# 获取当前目录及其所有子目录下的.py文件
for x in p.glob('*/*.py'):
    print(x)