n = int(input())
cur_cnt = 0

num = 666
while True:
    if str(num).find('666') > -1:
        cur_cnt += 1


    if cur_cnt == n:
        print(num)
        break

    num += 1