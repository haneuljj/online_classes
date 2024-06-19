# 국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 
# 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 
# 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
# 1.모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2.모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

# 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 
# 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 
# 그 합이 484로 가능한 최대가 된다. 

# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

N = int(input())

# 각 예산 요청 입력받아 리스트에 담기
budget = input().split()
budget = list(map(int, budget))
budget.sort()

total = int(input())

# 총예산보다 예산요청들의 합이 작거나 같을 경우 -> 가장 큰 예산요청값 출력
if(sum(budget) <= total):
    print(max(budget))
else:
    remainder = 0 # 나머지값 저장
    satisfied = 0 # 초과해서 요구하지 않는 경우
    temp = total // N
    remainder += (total % N)
    for i in budget:
        if temp - i >= 0:
            remainder += (temp - i)
            satisfied += 1

    temp2 = remainder // (len(budget) - satisfied)
    result = temp + temp2

    print(result)


##### 풀이
# 찾고자 하는 값 : 최적의 상한액
# 탐색 범위 : [0, 지방 요청 금액 중 최댓값]
N = int(input())
jibang = list(map(int, input().split()))
budget = int(input())

# 탐색범위 설정
left = 0
right = max(jibang)
answer = -1

while left <= right:
    middle = (left + right) // 2

    sum = 0
    for i in range(N):
        sum += min(middle, jibang[i])

    if sum <= budget:
        answer = middle
        left = middle + 1
    else:
        right = middle - 1

print(answer)