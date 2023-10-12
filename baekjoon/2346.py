N = int(input())
balloons = [i for i in range(1, N+1)]
paper = list(map(int, input().split()))

next = 0
while len(balloons):
    print(balloons[next], end=' ')
    
    balloons.pop(next)
    balloon = paper[next]
    paper.pop(next)

    if len(balloons) == 0:
        break

    if balloon > 0: balloon -= 1
    next = (next + balloon) % len(balloons)