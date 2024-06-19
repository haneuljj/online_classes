# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 
# 경우의 수를 구하는 프로그램을 작성하시오.

# 배열A에서 나올 수 있는 구간합이 M인 모든 경우의 수

N, M = map(int, input().split())
A = list(map(int, input().split()))

result = 0
main = 0
sub = 0

for i in range(N):

    while sub == N-1:
        if sum(A[main:sub+1]) == M:
            result += 1
            main += 1
            break
        if sum(A[main:sub+1]) > M:
            main += 1
            break
        else:
            sub += 1

print(result)

# 시작점이 움직일 때, 고려하지 않아도 되는 구간, 즉 합보다 작을걸 아는 구간도 계산

# 풀이
# 시작점 고정, 끝점을 한칸씩 옮기기
# 만약 합이 M이상이면 시작점 + 1
N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0 # 시작점
end = 0 # 끝점
sum = A[0] # 시작점 ~ 끝점의 구간합

count = 0
while True:
    # 현재 구간이 합이 M인지 확인
    if sum == M:
        count += 1

    # 구간 업데이트
    if sum >= M:
        start += 1
        sum -= A[start - 1]
    else:
        # 끝점이 이미 끝에 도달했을 때
        if end == N - 1:
            break

        end += 1
        sum += A[end]
    
print(count)


