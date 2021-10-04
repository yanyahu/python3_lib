import math

for i in range(6):
    print('{}/2 = {}'.format(i, math.modf(i / 2.0)))
"""modf() 接受一个浮点数并返回一个包含输入值的小数部分和整数部分的元组。"""
