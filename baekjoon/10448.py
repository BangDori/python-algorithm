import sys, itertools
input = sys.stdin.readline

gause = [0, 1]
for idx in range(2, 50):
    gause.append(gause[idx-1] + idx)
gause.pop(0)

test_case = int(input())
for _ in range(test_case):
    isSame = False
    num = int(input())

    end = len(gause)-1
    for idx in range(len(gause)):
        if gause[idx] >= num:
            end = idx-1
            break
    
    for numbers in itertools.product(gause[:end+1], repeat=3):
        if sum(numbers) == num:
            isSame = True
            break
    
    answer = 1 if isSame else 0
    print(answer)