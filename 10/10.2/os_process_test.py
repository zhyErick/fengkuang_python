import os
# 运行平台上的cmd命令
# os.system('cmd')
# 使用Excel打开xls文件
#os.startfile('C:\\Users\\Administrator\\Desktop\\huohua\\加班餐费.xlsx')
#os.spawnl(os.P_NOWAIT, 'C:\\Users\\Administrator\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe', ' ')
# 使用python命令执行os_test.py程序
os.execl("C:\python\venv\Scripts\python.exe", " ", 'os_test.py', 'i')