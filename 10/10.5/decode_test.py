import json
# 将json字符串恢复成python列表
result1 = json.loads('["yeeku", {"favorite": ["coding", null, "game", 25]}]')
print(result1)

# 将json字符串恢复成python字符串
result2 = json.loads('"\\"foo\\"bar"')
print(result2)

# 定义一个自定义的转换函数
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct
# 使用自定义的恢复函数
# 自定义的恢复函数将real数据转换成复数的实部,将imag转换为复数的虚部
result3 = json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
print(result3)

# 从文件流恢复json列表
f = open('a.json')
result4 = json.load(f)
print(result4)