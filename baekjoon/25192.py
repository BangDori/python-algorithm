# 채팅방의 기록 수 (N)
N = int(input())
record = {}

tot = 0
for i in range(N):
    chatting = input()

    if chatting == 'ENTER':
        record.clear()
        continue
    
    if not record.get(chatting):
        record[chatting] = 1
        tot += 1

print(tot)