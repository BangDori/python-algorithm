import math

a = int(input())

for i in range(1, a+1):
    num = i
    isMatch = False

    while i >= 1:
        if (i % 10 == 3) | (i % 10 == 6) | (i % 10 == 9):
            isMatch = True
            print('X', end='')
        elif (not isMatch) & (i < 10):
            print(num, end='')
            break

        i /= 10
        i = math.floor(i)
    
    print(end=' ')
