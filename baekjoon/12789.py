# 학생의 수 (N)
N = int(input())
students = list(map(int, input().split()))
students.reverse()
space = []

success = []
num = 1
isSuccess = True
while len(students) > 0 or len(space) > 0:
    if len(students) > 0:
        student = students[len(students)-1]

        if student == num:
            success.append(students.pop())
            num += 1
            continue
    
    if len(space) > 0:
        student = space[len(space)-1]

        if student == num:
            success.append(space.pop())
            num += 1
            continue

        if len(students) == 0:
            break
    
    space.append(students.pop())
    
if len(success) == N:
    print('Nice')
else:
    print('Sad')