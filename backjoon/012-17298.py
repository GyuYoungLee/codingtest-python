# 오큰수 구하기 (스택)

N = int(input())
A = list(map(int, input().split()))

answer = [0] * N
st = []

# [3 5 2 7] => 오큰수 [5 7 7 -1]
for i in range(N):
    while st and st[-1][0] < A[i]:  # 큰 수는 오큰수 처리
        _, idx = st.pop()
        answer[idx] = A[i]  # 오큰수 저장

    st.append((A[i], i))  # 작은 수는 스택에 저장

while st:
    _, idx = st.pop()
    answer[idx] = -1

for x in answer:
    print(x, end=' ')
