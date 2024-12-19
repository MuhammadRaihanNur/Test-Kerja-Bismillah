def ganteng(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

data = []
for i in range(100, 0, -1):
    if ganteng(i):
        continue
    if i % 15 == 0:
        data.append("FooBar")
    elif i % 3 == 0:
        data.append("Foo")
    elif i % 5 == 0:
        data.append("Bar")
    else:
        data.append(str(i))

print(", ".join(data) + ", %")
