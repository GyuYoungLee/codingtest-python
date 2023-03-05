# 최솟값 찾기 (슬라이딩 윈도우)

from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()

# 슬라이딩
for i in range(N):
    # 뒤쪽에 새로운 값 추가
    while dq and dq[-1][0] > A[i]:
        dq.pop()

    dq.append((A[i], i))  # (값, 인덱스) 디큐에 저장

    # 앞쪽에 기존 값 제거
    if dq[0][1] <= i - L:
        dq.popleft()

    print(dq[0][0], end=' ')  # 최소값 출력
