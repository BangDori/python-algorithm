num = int(input())
sum = 0
i = 1

while sum < num: 
    sum += i
    i += 1

if sum >= num:
    print(i-1)
else:
    print(i)