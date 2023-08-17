def GCD(distances):
    min_num = min(distances)
    gcd = 0

    while True:
        r = 0
        for item in distances:
            if item % min_num != 0:
                r = item % min_num

        if r == 0:
            gcd = min_num
            break

        min_num = r
    
    return gcd

# 가로수의 수 (N)
N = int(input())

trees = []
distances = []

isOdd = False
for i in range(N):
    tree = int(input())
    trees.append(tree)

    if i >= 1:
        distance = trees[i] - trees[i-1]

        if distance % 2 == 1:
            isOdd = True
        distances.append(distance)

gcd = GCD(distances)
tot_tree = 0
for item in distances:
    tot_tree += (item / gcd) - 1

print(int(tot_tree))