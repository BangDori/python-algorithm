import sys
input = sys.stdin.readline

N, M = map(int, input().split())
brandList = []

min_package_price = 1e9; min_each_price = 1e9
for _ in range(M):
    # 6줄 패키지, 낱개
    package_price, each_price = map(int, input().split())
    
    min_package_price = min(min_package_price, package_price)
    min_each_price = min(min_each_price, each_price)

if min_each_price * 6 < min_package_price:
    min_package_price = min_each_price * 6

package_count = N // 6
each_count = N % 6

# packge로 땜방하는 경우 vs package + each하는 경우
answer = min((package_count+1) * min_package_price, package_count * min_package_price + each_count * min_each_price)
print(answer)