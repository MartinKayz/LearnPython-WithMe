# Integer types
a = 13
b = 100
c = 66
print(a,b,c)
# knowing the type of variable
print(type(c))

# floating points
x = 33.5
y = 25.8
z = 205.0
print(x,y,z)
print(type(z))

# Complex types
d = 3 + 5j
print(d)
print(type(d))

# binary types
""" Begin with '0b' """
e = 0b10101
print(e)

# hexadecimal types
""" Begin with '0X' """
f = 0XFF
print(f)

# Octadecimal types
""" Begin with '0O' """
g = 0O234
print(g)

# boolean types
""" These carry two values
    True and False
"""
v = True
print(type(v))

# Type conversion functions
h = int(y) # converting floating point to interger
print(h)
print(type(h))

d = float("45.5") # converting string to floating point
print(d)
print(type(d))

# converting to binary
i = bin(10)
print(i)

# converting to hexadecimal
j = hex(10)
print(j)

# converting to octadecimal
k = oct(35)
print(k)


