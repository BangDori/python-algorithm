matrix = [[0 for _ in range(9)] for _ in range(9)]

max = 0
x = 1
y = 1

for i in range(9):
    matrix[i] = list(map(int, input().split()))
    new_matrix = matrix[i].copy()
    new_matrix.sort(reverse=True)

    if new_matrix[0] > max:
        max = new_matrix[0]
        x = i + 1
        y = matrix[i].index(max) + 1
    
print(max)
print(x, y)