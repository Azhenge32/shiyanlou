# for 循环的 else 子句给我们提供了检测循环是否顺利执行完毕的一种优雅方法。
for i in range(0, 5):
    print(i)
else:
    print("Bye bye")

for i in range(0, 5):
    print(i)
    if i == 2:
        break
else:
    print("Bye bye")