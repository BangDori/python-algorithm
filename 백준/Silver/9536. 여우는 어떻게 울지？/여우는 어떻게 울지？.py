import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    all_sound = input().rstrip().split()
    
    while True:
        try:
            animal, to, sound = input().rstrip().split()

            for i in range(len(all_sound)):
                if all_sound[i] == sound:
                    all_sound[i] = ""
        except:
            break
    
    for fox_sound in all_sound:
        if len(fox_sound) != 0:
            print(fox_sound, end=' ')