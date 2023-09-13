import sys
input = sys.stdin.readline

def getMax(quiz):
    split_quiz = ''
    max_quiz = []

    for q in quiz:
        split_quiz += q
        if q == 'K':
            max_quiz.append(split_quiz)
            split_quiz = ''
            continue

    if len(split_quiz) != 0:
        max_quiz.append(split_quiz)
        split_quiz = ''

    for idx, m in enumerate(max_quiz):
        M_count = m.count('M')

        if m[-1] == 'K':
            max_quiz[idx] = 5 * pow(10, M_count)
        else:
            max_quiz[idx] = '1' * M_count 
            
    for max in max_quiz:
        print(max, end='')

def getMin(quiz):
    split_quiz = ''
    min_quiz = []

    for q in quiz:
        split_quiz += q if q == 'M' else ''

        if q == 'K':
            if len(split_quiz) != 0:
                min_quiz.append(split_quiz)
                split_quiz = ''
            min_quiz.append(q)
            continue

    if len(split_quiz) != 0:
        min_quiz.append(split_quiz)
        split_quiz = ''

    for idx, m in enumerate(min_quiz):
        if m == 'K':
            min_quiz[idx] = 5
            continue
        M_count = m.count('M')
        min_quiz[idx] = pow(10, (M_count-1))

    for min in min_quiz:
        print(min, end='')

quiz = input().rstrip()

getMax(quiz)
print()
getMin(quiz)