from copy import copy
def euclid(a,b):
    """uses the euclidian algorithm to calc GCD of two numbers, a < b"""
    loop = 0
    value_dict = {a: [1,0],b:[0,1]}
    value = [1,0]
    while a != b and b != 1:
        c = a - b
        value = [value[0],value[1]-1]
        loop += 1
        if c < b:
            a = copy(b)
            b = copy(c)
        else:
            a = copy(c)
        print(a,b)
    return b,loop,value
x1 = int(input("Largest number "))
x2 = int(input("Smaller number "))

print(euclid(x1,x2))

