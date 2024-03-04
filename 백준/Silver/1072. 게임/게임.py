import sys
input = sys.stdin.readline

MAX_COUNT = 1000000000

def is_not_change_ratio(win_ratio):
    return win_ratio >= 99

def get_min_change_count(left, right, win_ratio):
    middle = (left + right) // 2
    min_change_count = 0

    while left <= right:
        middle = (left + right) // 2
        next_win_ratio = (win_count + middle) * 100 // (game_count + middle)
        
        if next_win_ratio > win_ratio:
            min_change_count = middle
            right = middle - 1
        else:
            left = middle + 1
    
    return min_change_count

game_count, win_count = map(int, input().split())
win_ratio = win_count * 100 // game_count

answer = 0
if is_not_change_ratio(win_ratio): answer = -1
else:
    answer = get_min_change_count(1, MAX_COUNT, win_ratio)

print(answer)