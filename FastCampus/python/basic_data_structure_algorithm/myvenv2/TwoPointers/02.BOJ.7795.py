# 심해에는 두 종류의 생명체 A와 B가 존재한다. 
# A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
# 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다.
# 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.
# 두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for i in B:
        for j in A:
            if i < j:
                count+=1

    print(count)
# --> 시간초과
# 두 배열을 정렬해놓는다면, B종이 더 큰게 명백하면 비교할 필요 없음
# B종에서 다 먹을 수 있는 A종을 발견하고 그거보다 더큰 수는 비교할 필요없음


# 풀이
# A배열을 가리키는 것(a) > B배열을 가리키는 것(b) 이면 B배열 포인터 이동
# a <= b이면, A배열 포인터 이동, 답 += sub인덱스(앞에 있는 원소 개수)
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = sorted(A)
    B = sorted(B)

    main = 0 # A배열 포인터
    sub = 0 # B배열 포인터
    count = 0

    # A 배열의 값을 다 돌때까지
    while main < N:
        # sub가 끝에 도달하면
        if sub == M:
            count += sub # 모든 B종 먹을 수 있음
            main += 1

        else:
            if A[main] > B[sub]: # A종이 B종보다 크면
                sub += 1 # B종 포인터 이동
            else:
                count += sub # 지금까지 이동된 앞의 원소 개수들 합해주기
                main += 1 # A종 포인터 이동
                
    print(count)
