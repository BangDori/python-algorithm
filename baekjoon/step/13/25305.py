# 응시자의 수 (n), 수상 학생 수 (k)
n, k = map(int, input().split())
score = list(map(int, input().split()))

score.sort(reverse=True)
print(score[k-1])