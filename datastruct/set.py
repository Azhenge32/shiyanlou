basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banaba'}
print(basket)
print('orange' in basket)
print('cafadf' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {'a', 'e', 'h', 'g'}
print(a.pop()) # 随机弹出
a.add('c')
print(a)