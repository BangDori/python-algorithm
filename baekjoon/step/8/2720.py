t = int(input()) # 테스트케이스

Quater = 25
Dime = 10
Nickel = 5
Penny = 1

for _ in range(t):
    c = int(input()) # 거스름돈

    print(c // Quater, end=' ')
    c = c - ((c // Quater) * Quater)
 
    print(c // Dime, end=' ')
    c = c - ((c // Dime) * Dime)
 
    print(c // Nickel, end=' ')
    c = c - ((c // Nickel) * Nickel)

    print(c // Penny)