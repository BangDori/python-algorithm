import sys
input = sys.stdin.readline

old_string = input().rstrip()
explosion_string = input().rstrip()

stack = []

for old_char in old_string:
    stack.append(old_char)

    if len(stack) >= len(explosion_string) and "".join(stack[len(stack)-len(explosion_string):]) == explosion_string:
        for _ in range(len(explosion_string)):
            stack.pop()

print("".join(stack) if len(stack) > 0 else "FRULA")