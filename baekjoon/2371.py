import sys
input = sys.stdin.readline

files_count = int(input())
files = []

file_length = 0
for _ in range(files_count):
    file = list(map(int, input().split()))
    file.pop()

    files.append(file)
    file_length = max(file_length, len(file))

answer = 0
for idx in range(file_length):
    file_idx = []

    for k, file in enumerate(files):
        if len(file) <= idx:
            file_idx.append(-k)
        else:
            file_idx.append(file[idx])
    
    file_set = set(file_idx)
    if len(file_set) == len(file_idx):
        answer = idx + 1
        break

print(answer)