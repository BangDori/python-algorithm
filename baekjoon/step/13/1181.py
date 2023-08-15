# 단어의 개수 (n)
n = int(input())
words = ["" for _ in range(n)]

for i in range(n):
    word = input()
    if words.count(word) == 0:
        words[i] = word

words.sort(key= lambda word : (len(word), word))

for i in range(words.count(""), n):
    print(words[i])