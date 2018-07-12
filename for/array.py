a = [1, 342, 223, 'India', 'Fedora']
print(a)
print(a[0])
print(a[4])
print(a[-1])

# f分片
print(a[0:-1])
print(a[2:-2])
print(a[:])
print(a[:-2])
print(a[-2:])
# 所有是有范围的
print(a[-5])
print(a[4])
# print(a[-7])
# print(a[5])

print(a[2:32])
print(a[32:])
# 从1开始，每隔两个元素取值
print(a[1::2])

# 增删改
a += [36, 49, 64, 81, 100]
print(a)

letters = ['a', 'b', 'c', 'c', 'd', 'f', 'g']
print(letters)
letters[2:5]=['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

# 检查值
a = ['ShiYanLou', 'is', 'cool']
print('cool' in a)
print('Linux' in a)
print(len(a))

# 检测列表是否为空
a = []
if a:
    print("列表为空")

# 嵌套列表
a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)
print(x[0])
print(x[0][1])