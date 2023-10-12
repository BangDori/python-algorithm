r = 31
M = 1234567891

# 문자열의 길이
L = int(input())
# 문자열
str = list(input())

sum = 0
for i in range(len(str)):
    a = ord(str[i]) - 96
    sum += (a * pow(r, i))
print(sum % M)