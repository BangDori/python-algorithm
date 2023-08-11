def convert(alpha):
    score = alpha[0]

    if alpha == 'A+':
        score = 4.5
    elif alpha == 'A0':
        score = 4.0
    elif alpha == 'B+':
        score = 3.5
    elif alpha == 'B0':
        score = 3.0
    elif alpha == 'C+':
        score = 2.5
    elif alpha == 'C0':
        score = 2.0
    elif alpha == 'D+':
        score = 1.5
    elif alpha == 'D0':
        score = 1.0
    else:
        score = 0
    
    return score


tot_grade = 0
tot_score = 0

for _ in range(20):
    subject = input().split()

    if subject[2] == 'P':
        continue

    tot_score += (float(subject[1]) * convert(subject[2]))
    tot_grade += (float(subject[1]))

print("%.6f" % (tot_score / tot_grade))