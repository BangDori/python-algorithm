import sys
input = sys.stdin.readline

MONEY = 1000
payment = int(input())
change_money = MONEY - payment

changes = [500, 100, 50, 10, 5, 1]
answer = 0

for change in changes:
    answer += change_money // change
    change_money = change_money - (change * (change_money // change))

print(answer)