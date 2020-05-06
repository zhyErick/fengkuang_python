from tkinter import *
# 定义继承Frame的Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 调用initWidgets()方法初始化界面
        self.initWidgets()
    def initWidgets(self):
        # 创建label对象,第一个参数只当将改Label放入root内
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file='images/serial.png')
        # 必须用一个不会被释放的变量引用该图片,否则图片会被收回
        w.x = bm
        # 设置显示的图片是bm
        w['image'] = bm
        w.pack()
        # 创建button对象,第一个参数指定将该Button放入root内
        okButton = Button(self, text="确定")
        okButton['background'] = "yellow"
        #okButton.configure(background='yellow') # 与上面代码的作用相同
        okButton.pack()
# 创建app对象
app = Application()
# Frame有一个默认的master属性,该属性值是Tk对象(窗口)
print(type(app.master))
# 通过master属性来设置窗口标题
app.master.title('窗口标题')
# 启动主窗口消息循环
app.mainloop()