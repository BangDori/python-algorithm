def permutation(output: list, start: int, last: int, count: int):
    if start == last:

        for n in output:
            print(n, end=' ')
        print()
        return
    else:
        for item in range(1, count+1):
            if output[len(output) - 1] > item:
                continue

            permutation(output + [item], start+1, last, count)


# 1 ~ N 중복 없이 M 개를 고른 수열
N, M = map(int, input().split())

for item in range(1, N+1):
    permutation([item], 1, M, N)