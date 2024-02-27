import sys
input = sys.stdin.readline

def sum_num(serial):
    result = 0

    for character in serial:
        if character.isdigit():
            result += int(character)
    
    return result

N = int(input())
serial_list = [input().strip() for _ in range(N)]

serial_list.sort(key=lambda serial: (len(serial), sum_num(serial), serial))

print("\n".join(serial_list))