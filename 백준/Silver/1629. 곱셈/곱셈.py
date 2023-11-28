import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def fpow(coef, exp, mod):
	if exp == 1:
		return coef % mod
	else:
		res = fpow(coef, exp//2, mod)
		if exp % 2 == 0:
			return (res * res) % mod
		else:
			return (res * res * coef) % mod

a, b, c = map(int, input().split())
result = fpow(a, b, c)
print(result % c)