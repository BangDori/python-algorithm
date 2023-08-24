while True:
    var = list(map(int, input().split()))

    if var.count(0) == 3:
        break

    var.sort()

    if pow(var[2], 2) == pow(var[0], 2) + pow(var[1], 2):
        print('right')
    else:
        print('wrong')