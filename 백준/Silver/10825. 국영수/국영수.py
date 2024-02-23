import sys
input = sys.stdin.readline

N = int(input())
students = []

for _ in range(N):
    student, korean, english, math = input().strip().split()
    korean = int(korean); english = int(english); math = int(math)

    students.append([student, korean, english, math])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])