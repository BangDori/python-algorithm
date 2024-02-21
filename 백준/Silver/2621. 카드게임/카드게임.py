import sys
input = sys.stdin.readline

COLOR_DICT = { 'R': 0, 'B': 1, 'Y': 2, 'G': 3}

colors = [0] * 4
cards = []
numberCount = [0] * 10

for i in range(5):
    color, number = input().strip().split()
    number = int(number)

    colors[COLOR_DICT[color]] += 1
    cards.append(number)
    numberCount[number] += 1
cards.sort()

# 1. 카드 5장이 모두 동일한 색이면서 연속적인 수일 경우
answer = 0
for i in range(4):
    if colors[i] != 5: continue

    isContinously = True
    for i in range(1, 5):
        if cards[i] - cards[i-1] != 1:
            isContinously = False
    
    if isContinously:
        answer = cards[-1] + 900

# 2. 5장 중 4장의 숫자가 동일할 때 800을 더한다
for i in range(1, 10):
    if numberCount[i] == 4:
        answer = max(answer, i + 800)

# 3. 3장의 숫자가 같고, 나머지 2장의 숫자도 같을 때 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 + 700
first = 0; second = 0
for i in range(1, 10):
    if numberCount[i] == 3: first = i
    if numberCount[i] == 2: second = i

    if first != 0 and second != 0:
        answer = max(answer, 700 + first * 10 + second)
        break

# 4. 5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다. 예를 들어, 카드가 Y3, Y4, Y8, Y6, Y7 일 때 점수는 608(=8+600)점이다.
for i in range(4):
    if colors[i] == 5:
        answer = max(answer, 600 + max(cards))
        break

# 5. 카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다. 예를 들어 R7, R8, G9, Y6, B5 일 때 점수는 509(=9+500)점이다.
isContinously = True
for i in range(1, 5):
    if cards[i] - cards[i-1] != 1:
        isContinously = False

if isContinously:
    answer = max(answer, 500 + max(cards))

# 6. 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다. 예를 들어 R7, Y7, R2, G7, R5 일 때 점수는 407(=7+400)점이다.
for i in range(1, 10):
    if numberCount[i] == 3:
        answer = max(answer, 400 + i)

# 7. 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다. 예를 들어, R5, Y5, Y4, G9, B4 일 때 점수는 354(=5X10+4+300)점이다.
if numberCount.count(2) == 2:
    first = 0; second = 0
    for i in range(1, 10):
        if first == 0 and numberCount[i] == 2:
            first = i
            continue
        if first != 0 and numberCount[i] == 2:
            second = i
        
        if first != 0 and second != 0:
            answer = max(answer, 300 + second * 10 + first)
            break

# 8. 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다. 예를 들어, R5, Y2, B5, B3, G4 일 때 점수는 205(=5+200)점이다.
if numberCount.count(2) == 1:
    for i in range(1, 10):
        if numberCount[i] == 2:
            answer = max(answer, 200 + i)
            break

# 9. 위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다. 예를 들어, R1, R2, B4, B8, Y5 일 때 점수는 108(=8+100)점이다.
answer = max(answer, 100 + max(cards))

print(answer)