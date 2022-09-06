#!/usr/bin/env python3
from array import *

inputnum1 = 148432
inputnum2 = 147376

if inputnum1 > inputnum2:
    a = inputnum1
    b = inputnum2
else:
    a = inputnum2
    b = inputnum1

print("a =", a)
print("b =", b)

divtable = [[1, 0, 0, 1, a, b, 0]]

while divtable[0][5] != 0:
    q = divtable[0][4] // divtable[0][5]
    u1 = divtable[0][1]
    u2 = divtable[0][3]
    u3 = divtable[0][5]
    v1 = divtable[0][0] - (q * divtable[0][1])
    v2 = divtable[0][2] - (q * divtable[0][3])
    v3 = divtable[0][4] - (q * divtable[0][5])
    newrow = [u1, v1, u2, v2, u3, v3, q]
    print(newrow)
    divtable.insert(0, (newrow))

gcd = divtable[0][4]
x = divtable[0][0]
y = divtable[0][2]
print("gcd =", gcd)
print("x =", x)
print("y =", y)
print("(", a, "*", x, ")", "+", "(", b, "*", y, ")", "=", gcd)

# TODO: output the table in proper order (currently, oldest values are at higher indices)
