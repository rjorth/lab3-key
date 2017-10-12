a = list(range(1, 11))
cubes = list(map(lambda x: pow(x, 3), a))
print cubes

m = list(map(lambda x: (x + 1), a))
print m

a2 = [i for i in a if i >= 5]
print a2

numbers = [i*i for i in a if i % 2 != 0]
print numbers
