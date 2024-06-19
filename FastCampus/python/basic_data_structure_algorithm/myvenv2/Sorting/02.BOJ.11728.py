# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers1 = list(map(int, input().split()))

numbers2 = list(map(int, input().split()))

num_set = set(numbers1 + numbers2)

num_list = sorted(num_set)

for i in num_list:
    print(i, end=" ")


# 풀이 - 시간제한 1.5초
# 입력받은 배열이 이미 정렬되어 있음
# 각 배열의 앞에서부터 작은 숫자 먼저 넣기
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

pos1 = 0  # A 배열의 후보의 위치값
pos2 = 0  # B 배열의 후보의 위치값

while pos1 < N and pos2 < M:
    candidate1 = A[pos1] # A배열의 후보값
    candidate2 = B[pos2] # B배열의 후보값

    # 더 작은 후보값을 리스트에 추가
    if candidate1 < candidate2:
        C.append(candidate1)
        pos1 += 1
    else:
        C.append(candidate2)
        pos2 += 1

# 위의 과정이 끝나도 배열에 값이 남아있을때, 남은 숫자 뒤에 이어 붙이기
if pos1 != N:
    C.extend(A[pos1:N])
if pos2 != M:
    C.extend(B[pos2:M])

# 결과 출력
for i in range(N + M):
    print(C[i], end=" ")