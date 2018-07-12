data = {'kusha1': 'Fedora', 'kart_': 'Debian', 'Jace':'Mac'}
print(data)
print(data['kart_'])

data['parthan'] = 'Unbuntu'
print(data)

del data['kusha1']
print(data)

print('ShiYanLou' in data)

# 字典中的键必须是不可变类型，比如你不能使用列表作为键。
# dict() 可以从包含键值对的元组中创建字典。
data2 = dict((('Indian','Delhi'),('Bangladesh','Dhaka')))
print(data2)

for x, y in data.items():
    print("{} uses {}".format(x, y))

data = {}
data.setdefault('names', []).append('Ruby')
print(data)
data.setdefault('names', []).append('Python')
print(data)
data.setdefault('names', []).append('C')
print(data)

# print(data['foo'])
print(data.get('foo', 0))

# 同时遍历两个序列
a = ['Pradeepto', 'Kushal']
b = ['OpenSUSE', 'Fedora']
for x, y in zip(a, b):
     print("{} uses {}".format(x, y))