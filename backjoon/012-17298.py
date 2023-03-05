# 오큰수 구하기 (스택)

N = int(input())
A = list(map(int, input().split()))

answer = [0] * N
st = []

for i in range(N):
    while st and st[-1][0] < A[i]:
        _, idx = st.pop()
        answer[idx] = A[i]  # 오큰수

    st.append((A[i], i))  # (값, 인덱스) 스택에 저장

while st:
    _, idx = st.pop()
    answer[idx] = -1

for x in answer:
    print(x, end=' ')
