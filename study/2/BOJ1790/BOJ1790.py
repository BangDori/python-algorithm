import sys
input = sys.stdin.readline

N, K = input().rstrip().split()
minus = ""
number = ""
for idx in range(len(K)-1, len(K)+1):
    if idx <= 0:
        continue
    minus = "1" * (idx-1)
    minus += "0"

    num = (int(K) + int(minus)) // idx

    if len(str(num)) <= idx:
        number = str(num)
        break

answer = 0
if int(number) > int(N):
    answer = -1
else:
    start = int(number)*len(number)-int(minus)
    answer = number[int(K)-start]
print(answer)