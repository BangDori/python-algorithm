import sys
input = sys.stdin.readline

def init_alpha_dict():
    alpha_dict = {}
    for i in range(26): alpha_dict[chr(i+65)] = 0
    return alpha_dict

word_cnt = int(input())
words = [list(input().strip()) for _ in range(word_cnt)]
alpha_dict = init_alpha_dict()

for word in words:
    for i in range(len(word)):
        num = 10 ** (len(word) - i - 1)
        alpha_dict[word[i]] += num

alpha_list = []
for value in alpha_dict.values():
    if value > 0:
        alpha_list.append(value)
alpha_list.sort()

answer = 0
for pow in range(9, 0, -1):
    if not alpha_list:
        break
    answer += pow * alpha_list.pop()

print(answer)