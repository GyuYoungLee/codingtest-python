import sys

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(sys.stdin.readline())

st = []
num = 1
answer = ""

for i in range(N):
    while num <= A[i]:
        answer += "+\n"
        st.append(num)
        num += 1

    if st[-1] == A[i]:
        answer += "-\n"
        st.pop()
    else:
        answer = "NO"
        break

print(answer)
