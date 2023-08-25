def recursion(s, l, r, count):
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)

T = int(input())

for _ in range(T):
    word = input()

    result, count = recursion(word, 0, len(word)-1, 1)
    print(result, count)