src_list = [12, 45, 3.5, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
statistics = {}
for ele in src_list:
    # 如果字典中包含ele代表的key
    if ele in statistics:
        # 将ele元素代表的出现次数加1
        statistics[ele] += 1
    # 如果字典中不包含ele代表的key,说明该元素还未出现过
    else:
        # 将ele元素代表的出现次数设为1
        statistics[ele] = 1
# 遍历dict,打印各元素出线的次数
for ele,count in statistics.items():
    print("%s 出线的次数为: %d" % (ele, count))