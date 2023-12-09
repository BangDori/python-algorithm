import sys
input = sys.stdin.readline

enable, waiting_length = map(int, input().split())
waiting_dict = {}

order = 0
for _ in range(waiting_length):
    sid = input().rstrip()

    waiting_dict[sid] = order
    order += 1

stack = list(waiting_dict)
stack.sort(key=lambda v: waiting_dict[v])
for i, sid in enumerate(stack):
    if i < enable:
        print(sid)

# 2 2
# 00000000
# 00000000