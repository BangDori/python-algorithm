# 카드의 개수 (n), 카드의 최대 합(m)
n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 인덱스 기준 (최대 개수)
cards_count = len(cards)

max_sum = 0
for x in range(cards_count):
    for y in range(x+1, cards_count):
        for z in range(y+1, cards_count):
            cur_sum = cards[x] + cards[y] + cards[z]
            if (cur_sum <= m) & (cur_sum > max_sum):
                max_sum = cur_sum

            if max_sum == m:
                break

        if max_sum == m: 
            break

    if max_sum == m:
        break

print(max_sum)