import sys
input = sys.stdin.readline

N = int(input())

books = {}
bid = 0

for _ in range(N):
    name = input().strip()

    if not books.get(name):
        books[name] = 0
    books[name] += 1

books_info = []
for name, count in zip(books.keys(), books.values()):
    books_info.append((name, count))

books_info.sort(key=lambda v: (-v[1], v[0]))
print(books_info[0][0])