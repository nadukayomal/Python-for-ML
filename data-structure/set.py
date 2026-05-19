x = {'kamal', 'sachin', 'rajitha'}
print(x)

x = {'kamal', 'sachin', 'rajitha', 'kamal'}
print(x)

x.add('sachin')
x.add('Kamal')
print(x)
x.remove('sachin')
print(x)

# combine sets
y = {'Technology', 'Mathematics', 'Bio'}
z = x.union(y)
print(z)

# diference sets 

x = {'kamal', 'sachin', 'rajitha'}
y = {'sachin', 'rajitha', 'perera'}

print(x.difference(y))
print(y.difference(x))