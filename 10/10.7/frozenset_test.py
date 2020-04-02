s = set()
frozen_s = frozenset('kotlin')
# 为set集合添加frozenset
s.add(frozen_s)
print(s)
sub_s = {'python'}
s.add(sub_s)