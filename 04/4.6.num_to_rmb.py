'''
把一个浮点数分解成整数部分和小数部分字符串
num 是需要被分解的浮点数
返回分解出来的整数部分和小数部分
第一个数组元素是整数部分,第个数组元素是小数部分
'''
def divide(num):
    # 将一个浮点数强制类型转换为int类型,即的到它的整数部分
    integer = int(num)
    # 浮点数部分减去整数部分,得到小数部分,小数部分乘以100后再取整,得到2位小数
    fraction = round((num - integer) * 100)
    # 下面把整数转换为字符串
    return (str(integer), str(fraction))


han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
unit_list = ['十', '百', '千']

'''
把一个4位数的数字字符串变成汉字的字符串,num_str事需要被转换的4位数字字符串,返回4位数字字符串被转换为汉字字符串
'''
def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    for i in range(num_len):
        # 把字符串变换为数值
        num = int(num_str[i])
        # 如果不是最后一位数字,而且数字不为零,则需要添加单位(千,百,十)
        if i != len(num_str) - 1 and num != 0:
            result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不要添加单位
        else:
            result += han_list[num]
    return result


'''
把数字字符串换成汉字字符串,num_str是需要被转换的数字字符串,返回数字字符串被转换成汉字字符串
'''
def integer_to_str(num_str):
    str_len= len(num_str)
    if str_len > 12:
        print('数字太大,翻译不了')
        return
    # 如果大于8位,包含单位"亿"
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + "亿" + four_to_hanstr(num_str[-8:-4]) + "万" + four_to_hanstr(num_str[-4:])
    # 如果大于4位,包含单位"万"
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4]) + "万" + four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)

num = float(input('请输入一个浮点数:'))
# 测试把一个浮点数分解成整数部分和小数部分
integer, fraction = divide(num)
print(integer_to_str(integer))
print(fraction)