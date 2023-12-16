import sys
input = sys.stdin.readline

def convert_number_type_time(time):
    hour, minute = map(int, time.split(":"))
    return hour * 100 + minute

start_time, end_time, final_end_time = input().rstrip().split()
start_time = convert_number_type_time(start_time)
end_time = convert_number_type_time(end_time)
final_end_time = convert_number_type_time(final_end_time)

# 이름이 등록되어 있다면 입장
# 이름의 값이 1이라면 참석 완료
meeting = {}

while True:
    try:
        chat_time, chat_nickname = input().rstrip().split()
        chat_time = convert_number_type_time(chat_time)

        # 입장 완료
        if chat_time <= start_time:
            meeting[chat_nickname] = 0
            continue
        
        if end_time <= chat_time <= final_end_time:
            if meeting.get(chat_nickname) == 0:
                meeting[chat_nickname] = 1
    except:
        break

answer = sum(meeting.values())
print(answer)