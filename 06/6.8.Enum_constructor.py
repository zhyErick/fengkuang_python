import enum
class Gender(enum.Enum):
    MAIL = '男', '阳刚之力'
    FEMAIL = '女', '柔顺之美'
    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc
    @property
    def desc(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name

# 访问FEAMIL的name
print('FEMAIL的name:', Gender.FEMAIL.name)
# 访问FEMAIL的value
print('FEMAIL的value:', Gender.FEMAIL.value)
# 访问自定义的cn_name属性
print('FEMAIL的cn_name:', Gender.FEMAIL.cn_name)
# 访问自定义的desc属性
print('FEMAIL的des:', Gender.FEMAIL.desc)