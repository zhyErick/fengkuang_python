class AuctionException(Exception): pass


class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            # 此处只是简单的打印异常信息
            print("转换出现异常")
            # 再次引发自定义异常
            # raise AuctionException("竞拍价必须是数值,不能包含其他字符!")
            raise AuctionException(e)
        if self.init_price > d:
            raise AuctionException("竞拍价比起拍价低,不允许竞拍!")
        initPrice = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid("dd")
    except AuctionException as ae:
        # 再次捕获到bid()方法中的异常,并对该异常进行处理
        print('main函数捕获异常', ae)

main()