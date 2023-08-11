start = int(input())
end = int(input())

sum = 0
isFirst = 0

if start == 2:
    start = 3
    sum += 2
    isFirst = 2

if start == 1:
    start = 2


for i in range(start, end+1):
    isPrime = True

    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    
    if isPrime:
        sum += i

        if isFirst == 0:
            isFirst = i

if sum > 0:
    print(sum)
    print(isFirst)
else:
    print(-1)