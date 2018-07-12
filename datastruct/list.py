a = [23, 45, 1, -3434, 234531, 234]
a.append(45)
print(a)

a.insert(0 ,111)
print(a)

print(a.count(45))

a.remove(45)
print(a)

a.reverse()
print(a)

b = [45, 56, 90]
a.extend(b)
print(a)

a.sort()
print(a)

del a[-1]
print(a)