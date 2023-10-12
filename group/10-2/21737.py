import sys
input = sys.stdin.readline

def calculate(x, y, sign):
    if sign == 'S':
        return x-y
    elif sign == 'M':
        return x*y
    elif sign == 'P':
        return x+y
    else:
        return -(abs(x)//y) if x < 0 else x//y

sign_count = int(input().rstrip())
form = list(input().rstrip())

if form.count('C') <= 0:
    print("NO OUTPUT")
else:
    first_num = 0
    current_num = 0
    sign = ''
    isC = False
    answer = []

    for val in form:
        if val.isdigit():
            current_num = current_num * 10 + ord(val) - ord('0')
        else:
            if isC:
                answer.append(first_num)
                isC = False
            elif len(sign) > 0:
                result = calculate(first_num, current_num, sign)
                first_num = result
            else:
                first_num = current_num

            current_num = 0
            if val == 'C':
                isC = True
            else:
                sign = val

    if isC:
        answer.append(first_num)

    for ans in answer:
        print(ans, end=' ')