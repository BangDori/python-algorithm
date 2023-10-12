import sys
input = sys.stdin.readline

course_length, running_length = map(int, input().split())

courses = list(map(int, input().split()))

reverse_courses = courses.copy()
reverse_courses.reverse()

courses += reverse_courses

answer = -1
for idx, course in enumerate(courses):
    if idx == 0:
        running_length -= (course-1)
    else:
        running_length -= course

    if running_length <= 0:
        if idx+1 > course_length:
            answer = course_length - (idx % course_length)
        else:
            answer = idx+1
        break
print(answer)