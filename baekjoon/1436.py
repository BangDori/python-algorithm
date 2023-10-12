N = int(input())

start = 666
count = 0
while True:
    if str(start).find('666') != -1:
        count += 1
    
    if count == N:
        print(start)
        break

    start += 1