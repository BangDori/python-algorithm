import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.left = 0
        self.right = 0
        self.value = value
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right

node = []
while True:
    try:
        node.append(int(input()))
    except:
        break

root = Node(node[0])
for i in range(1, len(node)):
    n = root

    while True:
        if n.value < node[i]:
            if n.right == 0:
                n.right = Node(node[i])
                break
            n = n.right
        else:
            if n.left == 0:
                n.left = Node(node[i])
                break
            n = n.left

def post_traverse(node):
    if node == 0:
        return
    
    post_traverse(node.left)
    post_traverse(node.right)
    print(node.value)

post_traverse(root)