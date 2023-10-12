import sys
input = sys.stdin.readline

rock_count = int(input())

if rock_count % 2 == 1:
    print("SK")
else:
    print("CY")