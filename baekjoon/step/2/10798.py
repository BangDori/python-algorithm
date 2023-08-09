matrix = [[-1 for _ in range(15)] for _ in range(5)]

endline = 0

for i in range(5):
    str = input()
    for j in range(len(str)):
        matrix[i][j] = str[j]

for i in range(15):
    endline = 0
    for j in range(5):
        if matrix[j][i] == -1:
            endline += 1
        else:
            print(matrix[j][i], end='')
    if endline == 5:
        break
