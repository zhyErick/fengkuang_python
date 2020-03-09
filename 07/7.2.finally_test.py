import os
def test():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e:
        print(e.strerror)
        # return语句强制方法返回
        # return
        os._exit(1)
    finally:
        # 关闭磁盘文件,回收资源
        if fis is not None:
            try:
                # 关闭资源
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行filnally块里的资源回收")

test()