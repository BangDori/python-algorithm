import sys
input = sys.stdin.readline

def dfs(friend):
    friend_list.remove(friend)

    connection_friend = friend_dict.get(friend)
    for next_friend in connection_friend:
        if friend_list.count(next_friend) != 0:
            dfs(next_friend)

test_case = 0
while True:
    test_case += 1
    friend_count = int(input())

    if friend_count == 0:
        break

    friend_dict = {}
    friend_list = []
    for _ in range(friend_count):
        friend1, friend2 = input().rstrip().split()

        if not friend_dict.get(friend1):
            friend_dict[friend1] = []
        if not friend_dict.get(friend2):
            friend_dict[friend2] = []
        
        friend_dict[friend1].append(friend2); friend_dict[friend2].append(friend1)
        friend_list.append(friend1); friend_list.append(friend2)
    
    count = 0
    while friend_list:
        friend = friend_list.pop()
        count += 1
        dfs(friend)
    
    print(test_case, count)