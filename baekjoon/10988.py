word = input()
cur_word = word[::-1]

if word == cur_word:
    print(1)
else:
    print(0)