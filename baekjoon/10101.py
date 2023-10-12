a = int(input())
b = int(input())
r = int(input())

if a + b + r == 180:
    if a == b == r == 60:
        print('Equilateral')
    elif (a == b) | (b == r) | (r == a):
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')