def permutation(output: list, start: int, last: int, count: int):
    if start == last:

        for n in output:
            print(n, end=' ')
        print()
        return
    else:
        for item in range(1, count+1):
            permutation(output + [item], start+1, last, count)


# 1 ~ N 중복 없이 M 개를 고른 수열
N, M = map(int, input().split())
permutation([], 0, M, N)