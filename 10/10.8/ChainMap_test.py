from collections import ChainMap
# 定义三个dict对象
a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}
# 将三个dict对象链再一起,就像变成一个大dict
cm = ChainMap(a, b, c)
print(cm)
# 获取Kotilin对应的value
print(cm['Kotlin'])
# 获取python对应的value
print(cm['Python'])

print(cm['Go'])