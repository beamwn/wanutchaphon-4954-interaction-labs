a = float(input('Enter a number: '))
b = float(input('Enter a number: '))

c=a+b

print(f'{a} + {b} = '+ str(c))

d = (f'{a} + {b} = '+ str(c))

print('Writing to file numberrs.txt')
print('Reading from file numbers.txt')
with open('numbers.txt', 'w') as w:
    w.write(d)

with open('numbers.txt', 'r') as r:
    s = r.read()

print(s)