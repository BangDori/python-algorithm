import sys
input = sys.stdin.readline

MAX_NUMBER = 1000000
numbers = [0, ]

num = 1
while len(numbers) <= MAX_NUMBER:
    temps = []
    temp = num

    while temp > 0:
        temps.append(temp%10)
        temp //= 10
    
    unique_temps = set(temps)
    if len(unique_temps) == len(temps):
        numbers.append(num)
    
    num += 1

while True:
    n = int(input())

    if n == 0:
        break

    print(numbers[n])