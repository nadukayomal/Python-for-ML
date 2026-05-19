x = {'100':'Colombo 7', '200':'Mauntlevenia', '150':'Kandy' }
x['300'] = 'Mawanella'

print(x)
print(x.keys())
print(x.values())

y = x['100']
print(y)

x['400'] = ['Malabe', 'Gampha']

print(x)


# Operations in Dictioanary

y = x.get(3, 0)
z = x.get('100', 10)
print(y)
print(z)

x = {
    'a' : ['hey', 'Good morning'],
    'b' : ['Hi', 'Good evening'],
    'c' : ['Hello', 'Good afternoon']
}


print(x)
y = x['a']
y.append('and Ayubovan')
print(x)