while True:
    n = int(input())

    # 탈출
    if n == -1:
        break
    
    sum = 0 # 약수들의 합
    factor_list = []

    for i in range(1, n):
        if n % i == 0:
            factor_list.append(str(i))
            sum += i

    if sum == n:
        print(n, "=", " + ".join(factor_list))
    else:
        print(n, "is NOT perfect.")