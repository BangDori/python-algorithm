p, q = map(int, input().split())
factor = 0 # 약수의 개수
q_value = 0 # q번째 위치의 값

for i in range(1, p+1):
    if p % i == 0:
        factor += 1

    if q == factor:
        q_value = i
        break


print(q_value)