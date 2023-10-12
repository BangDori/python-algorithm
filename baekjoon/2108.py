import sys
input = sys.stdin.readline

N = int(input())

numbers = {}
sorted_numbers = []
sum = 0
max_count_num = 0
max_count = 0
order = 1
for _ in range(N):
    num = int(input())

    if not numbers.get(num):
        numbers[num] = 1
    else:
        numbers[num] += 1
    sum += num
    sorted_numbers.append(num)

    if numbers[num] > max_count:
        max_count = numbers[num]

sorted_numbers.sort()

count = 0
for number in sorted_numbers:
    if numbers[number] == max_count and count < 2 and number != max_count_num:
        max_count_num = number
        count += 1

print(round(sum/N)) # 산술평균
print(sorted_numbers[int(N/2)]) # 중앙값
print(max_count_num) # 최빈값
print(sorted_numbers[len(sorted_numbers)-1] - sorted_numbers[0]) # 범위
