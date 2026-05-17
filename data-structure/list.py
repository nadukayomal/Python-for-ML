# list has created to store set of data under the single variable
# best practices is the keep same data type data in same list otherwise programme may be hard or not clear

x = [10, 20, 30, 40]
y = [66, 77, 88, 22]

print(x[0])
print(x[3])
# print(x[4])

print(x)

x[0] = 100

print(x)

# add value to the list
x.append(200)
print(x)
# add value in needed space
x.insert(2, 500)
print(x)
#delete values 
x.remove(40) # this we mention the value not index
print(x)
x.pop(1) # this we mention the index
print(x)


c = x + y
print(c)
print(x*3)
# print(x-3) # error

is_10_in_x = 10 in x
print(is_10_in_x)
is_not_10_in_x = not 10 in x
print(is_not_10_in_x)