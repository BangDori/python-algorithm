import sys
input = sys.stdin.readline

people_count = int(input())
tips = [int(input()) for _ in range(people_count)]
tips.sort(reverse=True)

tot_tips = 0
for idx, tip in enumerate(tips):
    person_tip = tip - idx

    if person_tip < 0:
        continue
    tot_tips += person_tip

print(tot_tips)