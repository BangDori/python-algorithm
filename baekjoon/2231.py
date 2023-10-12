n = int(input())

creator = 0
for i in range(1, n):
    m = i # 생성자 m
    sum = m

    while m >= 1:
        sum += int((m % 10)) # 자릿수 더하기
        m /= 10
        
    if n == sum: # 동일하다면
        creator = i
        # print(i) # 생성자 출력
        break

print(creator)
