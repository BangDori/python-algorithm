import sys
input = sys.stdin.readline

def get_distance(cur, want):
    x1, y1 = keyboard_dict.get(cur)
    x2, y2 = keyboard_dict.get(want)

    return abs(x1-x2) + abs(y1-y2)

# 초기 설정
keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]
keyboard_dict = {}
for row in range(3):
    for col in range(len(keyboard[row])):
        keyboard_dict[keyboard[row][col]] = (row, col)

constant = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']

# 입력
left, right = input().split()
wanted_string = input().rstrip()

answer = 0
for want in wanted_string:
    dist = 0
    if want in constant:
        dist = get_distance(left, want)
        left = want
    else:
        dist = get_distance(right, want)
        right = want
    
    answer += (dist+1)

print(answer)