"""
    作者：段浩彬
    功能：货币兑换
    版本：1.0
    日期：2019/3/21
"""

# 汇率
USD_VS_RMB = 6.77

# 人民币输入
currency_str_value = input("请输入带单位的货币金额")

# 获取货币单位
unit = currency_str_value[-3:]

if unit == "CNY":
    # 获取的是人民币
    rmb_str_value = currency_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / USD_VS_RMB
    print("美元金额（USD）：", usd_value)
elif unit == "USD":
    # 获取的是美元
    usd_str_value = currency_str_value[:-3]
    usd_value = eval(usd_str_value)
    rmb_value = usd_value * USD_VS_RMB
    print("人民币金额（CNY）:", rmb_value)
else:
    print("目前版本尚不支持该种货币")
