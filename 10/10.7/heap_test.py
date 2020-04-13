from heapq import *
my_data = list(range(10))
my_data.append(0.5)
# 此时my_data依然是一个list列表
print('my_data的元素', my_data)
# 对my_data应用堆属性
heapify(my_data)
print('应用堆之后my_data的元素:', my_data)
heappush(my_data, 7.2)
print(my_data)

# 弹出堆中最小的两个元素
print(heappop(my_data))
print(heappop(my_data))
print('弹出两个元素之后my_data的元素:', my_data)