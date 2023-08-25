import sys
input = sys.stdin.readline

count = 0

def merge_sort(A, p, r): # A[p..r]을 오름차순 정렬한다.
    if count == K:
        return
    if p < r:
        q = int((p + r)/2) # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    global count

    i = p
    j = q + 1
    t = 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i] # tmp[t] <- A[i]; t++; i++;
            i += 1
        else: 
            tmp[t] = A[j] # tmp[t] <- A[j]; t++; j++;
            j += 1
        count += 1
        if count == K:
            print(tmp[t])
            return
        t += 1
        
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        count += 1
        if count == K:
            print(tmp[t])
            return
        
        t += 1
        i += 1

    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        count += 1
        if count == K:
            print(tmp[t])
            return
        t += 1
        j += 1

    i = p
    t = 1
    while i <= r:  # 결과를 A[p..r]에 저장
        A[i] = tmp[t]
        i += 1
        t += 1

# 배열의 크기 (A), 저장 횟수 (K)
A, K = map(int, input().split())
array = list(map(int, input().split()))
tmp = [0 for _ in range(A+1)]

merge_sort(array, 0, len(array)-1)
if count < K:
    print(-1)