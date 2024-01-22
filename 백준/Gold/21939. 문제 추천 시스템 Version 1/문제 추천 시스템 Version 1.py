from heapq import heappush, heappop
import sys
input = sys.stdin.readline

RECOMMEND = 'recommend'
ADD = 'add'
SOLVED = 'solved'

problem_cnt = int(input())
min_heap = []
max_heap = []
problems = {}

def add_problem(pid, plevel):
    heappush(min_heap, (plevel, pid))
    heappush(max_heap, (-plevel, -pid))

    problems[pid] = True

def cleanup_max_heap():
    while not problems[-max_heap[0][1]]:
        heappop(max_heap)

def cleanup_min_heap():
    while not problems[min_heap[0][1]]:
        heappop(min_heap)

def solve_problem(pid):
    problems[pid] = False

for _ in range(problem_cnt):
    pid, plevel = map(int, input().split())
    add_problem(pid, plevel)

command_cnt = int(input())
recommend_problems = []
for _ in range(command_cnt):
    command = input().strip().split()

    if command[0] == RECOMMEND:
        if command[1] == '1':
            cleanup_max_heap()
            recommend_problems.append(-max_heap[0][1])
        else:
            cleanup_min_heap()
            recommend_problems.append(min_heap[0][1])    

    elif command[0] == ADD:
        pid, plevel = int(command[1]), int(command[2])
        add_problem(pid, plevel)

    else:
        pid = int(command[1])
        solve_problem(pid)

    cleanup_max_heap()
    cleanup_min_heap()

for answer in recommend_problems:
    print(answer)