# 转圈圈,
# 位于1号转弯线的行索引与列索引总和为n-1
# 位于2号转弯线的行索引与列索引相等
# 位于3号转弯线的行索引等于列索引减1


SIZE = 7
array = [[0] * SIZE]

# 创建一个长度为SIZE*SIZE的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]

# 该orient代表绕圈方向
# 其中0代表向下, 1代表向右, 2代表向左, 3代表向上
orient = 0
#控制将1~SIZE * SIZE的数填入二维列表中
# 其中j控制行索引, k控制列索引
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    # 如果位于1号转折线上
    if j + k == SIZE - 1:
        # j > k,位于左下角
        if j > k :
            orient = 1
        else:
            orient = 2
    # 如果位于2号折线上
    elif (k == j) and (k >= SIZE/2):
        orient = 3
    # 如果位于3号折线上
    elif (j == k -1) and (k <= SIZE/2):
        orient = 0
    # 根据方向来控制行索引,列索引的改变
    # 如果方向为向下绕圈
    if orient == 0:
        j += 1
    # 如果方向为向右绕圈
    elif orient == 1:
        k +=1
    # 如果方向为向左绕圈
    elif orient == 2:
        k -= 1
    # 如果方向为向上绕圈
    elif orient == 3:
        j -= 1

# 采用遍历输出上面的二维列表
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d ' % array[i][j], end="")
    print("")