import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def cantoa(N, order):
    if order == 2:
        print(' ' * N, end='')
        return
    
    if N == 1:
        print('-', end='')
        return

    cantoa(N//3, 1)
    cantoa(N//3, 2)
    cantoa(N//3, 3)

while True:
    try:
        N = int(input())
        cantoa(3 ** N, 1)
        print()
    except:
        break