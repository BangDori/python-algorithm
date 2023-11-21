import sys
input = sys.stdin.readline

ROOT = 'A'
EMPTY = '.'

def pre_traverse(node):
    if node == EMPTY:
        return

    left, right = tree.get(node)

    print(node, end='')
    pre_traverse(left)
    pre_traverse(right)

def in_traverse(node):
    if node == EMPTY:
        return
    
    left, right = tree.get(node)

    in_traverse(left)
    print(node, end='')
    in_traverse(right)

def post_traverse(node):
    if node == EMPTY:
        return
    
    left, right = tree.get(node)

    post_traverse(left)
    post_traverse(right)
    print(node, end='')

N = int(input())

tree = {}
for _ in range(N):
    parent, left, right = input().rstrip().split()
    tree[parent] = [left, right]

pre_traverse(ROOT)
print()
in_traverse(ROOT)
print()
post_traverse(ROOT)