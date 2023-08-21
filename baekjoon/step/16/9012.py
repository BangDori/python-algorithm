T = int(input())
parenthesis = []

for _ in range(T):
    quiz = input()

    while quiz.count('()'):
        quiz = quiz.replace('()', '')
    if len(quiz) > 0:
        print('NO')
    else:
        print('YES')