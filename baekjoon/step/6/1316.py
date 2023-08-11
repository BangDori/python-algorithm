t = int(input())
groupWordCount = 0

for _ in range(t):
    isGroupWord = True
    word = input()

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue

        if word.find(word[i], i+1) > 0:
            isGroupWord = False
    
    if isGroupWord:
        groupWordCount += 1

print(groupWordCount)