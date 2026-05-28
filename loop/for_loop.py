x = [1, 2 , 3 , 5, 7]

for item in x:
    print(item)

index = 0

for item in x:
    y = x[index]
    print(index, y)
    index += 1

for item in enumerate(x):
    # print(type(item), item)
    index = item[0]
    Value = item[1]
    print(index, Value)

print("\n")

for index, value in enumerate(x):
    print(index, value)

print("\n")

for item in range(0,10):
    print(item, type(item))