import heapq
import sys
input = sys.stdin.readline

RECOMMEND = 'recommend'
ADD = 'add'
SOLVED = 'solved'

# 문제의 수
N = int(input())
min_heap = []
max_heap = []
in_problems = {}

def add_problem(pid, level):
    heapq.heappush(min_heap, [level, pid])
    heapq.heappush(max_heap, [-level, -pid])

    in_problems[pid] = True

def cleanup_maxheap():
    while not in_problems[-max_heap[0][1]]:
        heapq.heappop(max_heap)

def cleanup_minheap():
    while not in_problems[min_heap[0][1]]:
        heapq.heappop(min_heap)

for _ in range(N):
    pid, level = map(int, input().split())
    add_problem(pid, level)

# 명령문의 수
M = int(input())
answer = []
for _  in range(M):
    command = input().rstrip().split()

    if command[0] == RECOMMEND:
        if command[1] == '1':
            cleanup_maxheap()
            answer.append(-max_heap[0][1])
        else:
            cleanup_minheap()
            answer.append(min_heap[0][1])

    elif command[0] == SOLVED:
        in_problems[int(command[1])] = False

    else:
        pid, level = int(command[1]), int(command[2])

        cleanup_maxheap(); cleanup_minheap()
        add_problem(pid, level)

for ans in answer:
    print(ans)