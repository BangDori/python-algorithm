import sys
input = sys.stdin.readline

option_count = int(input())
options = [[] for _ in range(option_count)]

checked = [False] * 26

for idx in range(option_count):
    option = input().split()
    options[idx] = option

    isCheck = False

    for jdx in range(len(option)):
        if not checked[ord(option[jdx][0].upper()) - 65]:
            checked[ord(option[jdx][0].upper()) - 65] = True

            check_option = '[' + option[jdx][0] + ']'
            option[jdx] = option[jdx].replace(option[jdx][0], check_option, 1)

            isCheck = True
            break

    if isCheck:
        continue

    for jdx in range(len(option)):
        for kdx in range(1, len(option[jdx])):
            if not checked[ord(option[jdx][kdx].upper()) - 65]:
                checked[ord(option[jdx][kdx].upper()) - 65] = True

                check_option = '[' + option[jdx][kdx] + ']'
                option[jdx] = option[jdx].replace(option[jdx][kdx], check_option, 1)

                isCheck = True
                break
        if isCheck:
            break

for option in options:
    print(" ".join(option))