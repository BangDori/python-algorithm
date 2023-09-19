import sys
input = sys.stdin.readline

house_count, wifi_count = map(int, input().split())
house = [int(input()) for _ in range(house_count)]
house.sort()

def binary_search(start, end):
    while start <= end:
        mid = (start+end) // 2
        cur = house[0]
        count = 1

        for h in range(1, len(house)):
            if house[h] >= cur + mid:
                count += 1
                cur = house[h]

        if count >= wifi_count:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = house[-1] - house[0]
answer = 0

binary_search(start, end)
print(answer)