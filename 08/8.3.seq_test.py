def check_key(key):
    '''
    该函数将会负责检查序列的索引,该索引必须是整数值,否则引发TypeError异常,
    且程序要求索引必须为非负整数值,否则引发IndexError异常
    '''
    if not isinstance(key, int): raise TypeError('索引值必须是整数')
    if key < 0: raise IndexError('索引值必须是非负整数')
    if key >= 26 ** 3: raise IndexError('索引值不能超过%d' % 26 ** 3)


class StringSeq:
    def __init__(self):
        # 用于存储被修改的数据
        self.__changed = {}
        # 用于存储被删除元素的索引
        self.__deleted = []

    def __len__(self):
        return 26 ** 3

    def __getitem__(self, key):
        # 根据索引获取序列中的元素
        check_key(key)
        # 如果self.__changed 中找到修改后的数据
        if key in self.__changed:
            return self.__changed[key]
        # 如果key在self.__deleted中,说明该元素已被删除
        if key in self.__deleted:
            return None
        # 否则根据计算规则返回序列元素
        three = key // (26 * 26)
        two = (key - three * 26 * 26) // 26
        one = key % 26
        return chr(65 + three) + chr(65 + two) + chr(65 + one)

    def __setitem__(self, key, value):
        # 根据索引修改序列中的元素
        check_key(key)
        # 将修改的元素以 key-value对的形式保存在__changed中
        self.__changed[key] = value

    def __delitem__(self, key):
        # 根据索引删除序列中的元素
        check_key(key)
        #  如果__deleted 列表中没有包含被删除的key,则添加被删除的key
        if key not in self.__deleted: self.__deleted.append(key)
        # 如果__changed中包含被删除的key,则删除它
        if key in self.__changed: del self.__changed[key]

# 创建序列
sq = StringSeq()
# 获取序列的长度,实际上就是返回__len__()方法的返回值
print(len(sq))
print(sq[26*26])
# 打印修改之前的sq[1]
print(sq[1])
# 修改sq[1]的元素
sq[1] = 'fkit'
#打印修改之后的sq[1]
print(sq[1])
# 删除sq[1]
del sq[1]
print(sq[1])

# 再次对sq[1]赋值
sq[1] = 'crazyit'
print(sq[1])