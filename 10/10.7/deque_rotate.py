from collections import deque
q = deque(range(5))
# 执行旋转,使之首尾相连
q.rotate()
print('q中的元素:', q)
# 再次旋转,使之首尾相连
q.rotate()
print('q中的元素:', q)