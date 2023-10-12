# 출입 기록의 수 (n)
n = int(input())
records = {}

for i in range(n):
    name, record = input().split()

    if record == 'enter':
        records[name] = record
    else:
        records.pop(name)

names = list(records.keys())
names.sort(reverse=True)

for i in range(len(names)):
    print(names[i])