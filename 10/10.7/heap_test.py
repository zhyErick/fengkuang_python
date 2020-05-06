from heapq import *
my_data = list(range(10))
my_data.append(0.5)
# 此时my_data 依然是一个list列表
print('my_data的元素:', my_data)
# 对my_data应用堆属性
heapify(my_data)
print('应用堆属性后my_data的元素:', my_data)

heappush(my_data, 7.2)
print('添加7.2之后my_data的元素:', my_data)

# 弹出堆中最小的元素
print(heappop(my_data))
print(heappop(my_data))
print('弹出2个元素之后my_data的元素:', my_data)

# 弹出最小的元素,压入指定元素
print(heapreplace(my_data, 8.1))
print('执行replace之后my_data的元素:', my_data)

print('my_data中最大的3个元素:', nlargest(3, my_data))
print('my_data中最小的4个元素:', nsmallest(4, my_data))