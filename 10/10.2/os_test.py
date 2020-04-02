import os
print(os.name)
# 获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))
# 返回当前系统的登录用户名
print(os.getlogin())
# 获取当前进程id
print(os.getppid())
# 获取当前进程的父进程的id
print(os.getppid())
# 返回当前系统的cpu的数量
print(os.cpu_count())
# 返回路径分隔符
print(os.sep)
# 返回当前系统的路径分隔符
print(os.pathsep)
# 返回当前系统的换行符
print(os.linesep)
# 返回适合加密使用的,最多由3个字节组成的bytes对象
print(os.urandom(3))