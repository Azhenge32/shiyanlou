import math
r = input("请输入半径:")
r = int(r)
print("{:.10000f}".format(r * math.pi))
print(round(r * math.pi, 10000))