import sys
input = sys.stdin.readline

file_count = int(input())
file_dict = {}

for _ in range(file_count):
    filename = input().rstrip()
    extension = filename.split('.')[1]

    if not file_dict.get(extension):
        file_dict[extension] = 1
        continue

    file_dict[extension] += 1

extensions = list(file_dict.keys())
extensions.sort()

for extension in extensions:
    print(extension, file_dict.get(extension))