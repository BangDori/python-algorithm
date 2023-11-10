import sys
input = sys.stdin.readline

def getMaxDiffLength(max_diff_count, sentence):
    ptr_dict = { }
    x, y = 0, 0
    diff_count, max_length = 0, 0

    while y < len(sentence):
        if ptr_dict.get(sentence[y]):
            ptr_dict[sentence[y]] += 1
            y += 1
            continue
        
        if not ptr_dict.get(sentence[y]) and diff_count < max_diff_count:
            ptr_dict[sentence[y]] = 1
            y += 1
            diff_count += 1
            continue
        
        max_length = max(max_length, y-x)
        
        ptr_dict[sentence[x]] -= 1
        if ptr_dict[sentence[x]] == 0:
            diff_count -= 1
        x += 1

    return max(max_length, y-x)

while True:
    M = int(input())

    if M == 0:
        break

    sentence = list(input().rstrip())
    answer = getMaxDiffLength(M, sentence)
    print(answer)