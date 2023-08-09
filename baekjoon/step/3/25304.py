tot_price = int(input())
tot_count = int(input())


for _ in range(tot_count):
    item_price, item_cnt = map(int, input().split())

    tot_price -= (item_price * item_cnt)

if tot_price == 0:
    print('Yes')
else:
    print('No')