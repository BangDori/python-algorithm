from itertools import combinations
import sys
input = sys.stdin.readline

def get_distance(a, b):
    distance = 0

    for x, y in zip(a, b):
        if x != y:
            distance += 1
    
    return distance


def get_total_distance(mbtis):
    a, b, c = mbtis

    distanceAB = get_distance(a, b)
    distanceBC = get_distance(b, c)
    distanceCA = get_distance(c, a)

    return distanceAB + distanceBC + distanceCA

T = int(input())
mbti = {}

for _ in range(T):
    mbti_count = int(input().rstrip())
    mbti_types = input().rstrip().split()

    if mbti_count > 32:
        print(0)
        continue

    for mbti_type in mbti_types:
        if not mbti.get(mbti_type):
            mbti[mbti_type] = 0

        mbti[mbti_type] += 1

    answer = sys.maxsize
    mbti_keys = list(mbti.keys())
    mbti_values = list(mbti.values())

    for mbtis in combinations(mbti_types, 3):
        distance = get_total_distance(mbtis)
        answer = min(answer, distance)

    print(answer)
    mbti.clear()