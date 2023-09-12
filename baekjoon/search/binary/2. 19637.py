import sys
input = sys.stdin.readline

def get_grade(character, values):
    left = 0
    right = len(values)-1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == character:
            break
        elif values[mid] > character:
            right = mid - 1
        else:
            left = mid + 1

    return values[mid] if left < mid else values[left]

grade_count, character_count = map(int, input().split())

# 등급 정보
grades = {}
for _ in range(grade_count):
    grade, value = input().split()

    if not grades.get(int(value)):
        grades[int(value)] = grade
values = list(grades.keys())
values.sort()

# 캐릭터 정보
characters = []
for _ in range(character_count):
    value = int(input())
    characters.append(value)

for character in characters:
    grade = get_grade(character, values)
    print(grades.get(grade))