max_size = 123456 * 2 + 1
array = [True] * max_size

array[0] = array[1] = False
for i in range(2, max_size):
    if array[i]:
        for j in range(i+i, max_size, i):
            array[j] = False

while True:
    num = int(input())

    if num == 0:
        break

    count = 0
    for i in range(num+1, num*2+1):
        if array[i]:
            count += 1
    print(count)