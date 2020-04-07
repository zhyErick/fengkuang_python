import time
# 将当前时间转换为时间字符串
print(time.asctime())

# 将指定时间转换为时间字符串,时间元组的后面3个元素没有设置
print(time.asctime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))
# 将以秒数代表的时间转换为时间字符串
print(time.ctime(30))

# 将以秒数代表的时间转换为struct_time对象
print(time.gmtime(30))

# 将当前时间转换为struct_time对象
print(time.gmtime())

# 将以秒数代表的时间转换为代表当前时间的struct_time对象
print(time.localtime())

# 将元组格式的时间转换为以秒数代表的时间
print(time.mktime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))

# 返回性能计数器的值
print(time.perf_counter())

# 返回当前进程使用cpu的时间
print(time.process_time())
# time.sleep(10)

# 将当前时间转换为指定格式的字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 将指定时间字符串恢复成struct_time对象
st = '2018年3月20日'
print(time.strptime(st, '%Y年%m月%d日'))

# 返回从1970年1月1日0点整到现在过了多少秒
print(time.time())

# 返回本地时区的时间偏移,以秒为单位
print(time.timezone)