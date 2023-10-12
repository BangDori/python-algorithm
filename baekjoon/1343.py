"""
    2 sec, 128 MB

    AAAA, BB

    ., X로 주어지는데, .를 제외하고 덮기

    입력
        ., X로 이루어진 보드
"""

import sys
input = sys.stdin.readline

board = input()
answer = board
answer = board.replace("XXXX", "AAAA")
answer = answer.replace("XX", "BB")

if answer.count('X'):
    print(-1)
else:
    print(answer)