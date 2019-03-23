"""
    作者：段浩彬
    功能：货币兑换
    版本：1.0
    日期：2019/3/21
"""


def convert_currency(im, er):
    """
        汇率兑换函数
    """
    out = im * er
    return out


# 汇率
USD_VS_RMB = 6.77
currency_str_value = input("请输入带单位的货币金额")
# 获取货币单位
unit = currency_str_value[-3:]
if unit == "CNY":
    exchange_rate = USD_VS_RMB
elif unit == "USD":
    exchange_rate = 1 / USD_VS_RMB
else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    # 调用函数
    out_money = convert_currency(in_money, exchange_rate)
    print('转换后的金额', out_money)
else:
    print('不支持该种货币')
print('程序已退出')
