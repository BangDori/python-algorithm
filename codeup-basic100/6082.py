n = int(input())

for i in range(1, n+1):
    num = str(i)
    count = num.count('3') + num.count('6') + num.count('9')

    if count > 0:
        print('X' * count, end=' ')
    else:
        print(num, end=' ')