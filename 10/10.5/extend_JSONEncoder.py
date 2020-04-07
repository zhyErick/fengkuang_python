import json
# 定义JSONEncodeer的子类
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        # 如果转换的对象是复数类型,程序负责处理
        if isinstance(obj, complex):
            return {"__complex__": 'true', 'real': obj.real, 'imag': obj.imag}
        # 对于其他类型,还是用JSONEncoder默认处理
        return json.JSONEncoder.default(self, obj)


s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
print(s1)

s2 = ComplexEncoder().encode(2 + 1j)
print(s2)