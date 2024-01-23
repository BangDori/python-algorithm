import sys
input = sys.stdin.readline

input_string = input().rstrip()
input_length = len(input_string)

if input_length == 1:
    print(input_string)
else:
    alphabets = {}
    for alpha in input_string:
        if not alphabets.get(alpha):
            alphabets[alpha] = 0
        alphabets[alpha] += 1

    alphabet_list = list(alphabets.keys())
    alphabet_list.sort()

    answer = ['' for _ in range(input_length)]
    curr = 0; isError = False

    while answer[curr] == '':
        isSearch = False

        for alpha in alphabet_list:
            if alphabets[alpha] >= 2:
                answer[curr] = alpha; answer[-(curr+1)] = alpha
                alphabets[alpha] -= 2
                curr += 1
                isSearch = True
                break
            
        if not isSearch:
            for alpha in alphabet_list:
                if alphabets[alpha] >= 1 and answer[curr+1] != '':
                    answer[curr] = alpha
                    alphabets[alpha] -= 1
                    curr += 1
                    isSearch = True
                    break
        
        if not isSearch:
            isError = True
            break

    if isError or len("".join(answer)) != input_length or answer != answer[::-1]:
        print("I'm Sorry Hansoo")
    else:
        print("".join(answer))