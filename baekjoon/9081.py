import sys
input = sys.stdin.readline

test_case = int(input().rstrip())

for _ in range(test_case):
    word = list(input().rstrip())

    x = 0; y = 0

    for idx in range(1, len(word)):
        if word[idx] > word[idx-1]:
            x = idx-1
    
    for idx in range(x+1, len(word)):
        if word[idx] > word[x]:
            y = idx

    if x == 0 and y == 0:
        print("".join(word))
    else:
        word[x], word[y] = word[y], word[x]

        word_cp = word[x+1:].copy()
        word_cp.reverse()
        word = word[:x+1] + word_cp

        print("".join(word))