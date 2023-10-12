a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a1 * n0 + a0 # ax+b
cn = c * n0 # cx

isTrue = True
for i in range(n0, 101):
    fn = a1*i + a0
    cn = c * i
    if fn <= cn:
        continue
    else:
        isTrue = False
        break

if isTrue:
    print(1)
else:
    print(0)