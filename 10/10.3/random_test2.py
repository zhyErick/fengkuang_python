import random
import collections
# 指定随机抽取6个元素,各元素被抽取权重(概率)不同
print(random.choices(['Python', 'Swift', 'Kotlin'], [5, 5, 1], k=6))
# 下面模拟从52张扑克牌中抽取20张
# 在被抽到的20张牌中,牌面为10()