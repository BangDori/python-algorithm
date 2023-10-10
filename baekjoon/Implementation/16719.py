import sys
input = sys.stdin.readline

quiz = list(input().rstrip())
quiz_copy = quiz.copy()
quiz_copy.sort()

answer = ["" for _ in range(len(quiz))]

init_alpha = quiz_copy.pop(0)
init_alpha_idx = quiz.index(init_alpha)
answer[init_alpha_idx] = init_alpha

print("".join(answer))
for idx in range(1, len(quiz)):
    prev_answer = "".join(answer)
    add_alpha = ""; add_idx = -1

    for alpha in quiz_copy:
        cur_idx = quiz.index(alpha)
        if quiz.count(alpha) >= 2:
            for jdx in range(len(quiz)-1, -1, -1):
                if quiz[jdx] == alpha:
                    cur_idx = jdx
                    break

        answer[cur_idx] = alpha

        if "".join(answer) < prev_answer or len(prev_answer) == idx:
            prev_answer = "".join(answer)
            add_alpha = alpha
            add_idx = cur_idx

        answer[cur_idx] = ""
    
    quiz[add_idx] = ""
    answer[add_idx] = add_alpha
    quiz_copy.pop(quiz_copy.index(add_alpha))
    print(prev_answer)