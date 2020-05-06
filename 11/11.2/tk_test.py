from tkinter import *
# 创建tk对象,Tk代表窗口
root = Tk()
# 设置窗口标题
root.title('窗口标题')
# 创建Label对象,第一个参数指定Label放入root内
w = Label(root, text="Hello Tkinter")
# 调用pack进行布局
w.pack()
# 启动窗口
root.mainloop()