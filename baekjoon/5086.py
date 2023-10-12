while True:
    x, y = map(int, input().split())

    # 탈출
    if (x == 0) & (y == 0):
        break

    # x가 y의 약수라면 factor
    if y % x == 0: 
        print('factor')
        continue

    # x가 y의 배수라면 multiple
    if x % y == 0:
        print('multiple')
        continue

    # 둘 다 아니라면 neither
    print('neither')