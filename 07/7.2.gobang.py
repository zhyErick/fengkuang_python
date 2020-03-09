# 定义棋盘大小
BOARD_SIZE = 15
# 定义一个二维列表来充当棋盘
board = []
def initBoard():
    # 为每个元素赋值"+",用于控制台画出棋盘
    for i in range(BOARD_SIZE):
        row = ["+"] * BOARD_SIZE
        board.append(row)

# 在控制台输出棋盘的方法
def printBoard():
    # 打印每个列元素
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # 打印完列元素不换行
            print(board[i][j], end="")
        # 每打印完一行列表元素后输出一个换行符
        print()
initBoard()
printBoard()
inputStr = input("请输入您下棋的坐标,应以x,y的格式: \n")
while inputStr != None:
    try:
        # 将用户输入的字符串以逗号(,)作为分隔符,分割成两个字符
        x_str, y_str = inputStr.split(sep=",")
        # 如果下棋的点不为空
        if board[int(y_str) - 1][int(x_str) - 1] != "+":
            inputStr = input("您输入的坐标点已有棋子了,请重新输入\n")
            continue
        # 把对应的坐标列表元素赋为"·"
        board[int(y_str) - 1][int(x_str) - 1] = "·"
    except Exception:
        inputStr = input("您输入的坐标不合法,请重新输入,下棋坐标应以x,y的格式\n")
        continue
    printBoard()
    inputStr = input("请输入您下棋的坐标,应以x,y的格式: \n")