N = 4
A = [9, 5, 4, 8]
answer = [0, 0, 0, 0]

st = []

for i in range(N):
    while st and st[-1][0] < A[i]:
        _, idx = st.pop()
        answer[idx] = A[i]

    st.append((A[i], i))

while st:
    _, idx = st.pop()
    answer[idx] = -1

for x in answer:
    print(x, end=' ')
