import sys
input = sys.stdin.readline

OK = "OK"
FAKE = "FAKE"

T = int(input())

for _ in range(T):
    alphabet_count = [0] * 26
    message = input().rstrip()

    isMessage = True
    for i, m in enumerate(message):
        k = ord(m)-65
        alphabet_count[k] += 1

        if alphabet_count[k] >= 3 and alphabet_count[k] % 4 == 3:
            if i == len(message)-1:
                isMessage = False
                break

            if message[i] != message[i+1]:
                isMessage = False
                break

    if isMessage:
        print(OK)
    else:
        print(FAKE)