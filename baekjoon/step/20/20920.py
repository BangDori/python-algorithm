import sys
input = sys.stdin.readline

# 단어의 개수 (N), 외울 단어의 길이 기준 (M)
N, M = map(int, input().split())
dict = {}

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    if not dict.get(word):
        dict[word] = 1
    else:
        dict[word] += 1

dict_list = []
for key in dict.keys():
    dict_list.append((key, dict[key]))

# 1. 사전 순 정렬
dict_list.sort(key= lambda item: item[0])
# 2. 길이 순 정렬
dict_list.sort(reverse=True, key= lambda item: len(item[0]))
# 3. 빈도 순 정렬
dict_list.sort(reverse=True, key= lambda item: item[1])

for word, count in dict_list:
    print(word)