number = input().strip()

count = 1
idx = 0
answer = -1

while True:
    for num in str(count):
        if number[idx] == num:
            idx += 1

            if idx >= len(number):
                answer = count
                break
    
    if answer != -1: break
    count += 1

print(answer)