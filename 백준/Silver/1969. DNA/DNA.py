import sys
input = sys.stdin.readline

NumberToDNA = { 0: "A", 1: "C", 2: "G", 3: "T" }
DNAToNumber = { "A": 0, "C": 1, "G": 2, "T": 3 }

dnaCount, length = map(int, input().split())
dnaList = [list(input().strip()) for _ in range(dnaCount)]

dnaCountList = [[0, 0, 0, 0] for _ in range(length)]

for dna in dnaList:
    for i, alpha in enumerate(dna):
        dnaCountList[i][DNAToNumber[alpha]] += 1

answerDNA = ""
answerCount = 0
for i, digit in enumerate(dnaCountList):
    maxCount = max(digit)
    maxCountPos = dnaCountList[i].index(maxCount)

    answerDNA += NumberToDNA[maxCountPos]
    answerCount += dnaCount - maxCount

print(answerDNA, answerCount, sep='\n')