# 학교에서 그래픽스 수업을 들은 동준이는 수업시간에 들은 내용을 바탕으로 스마트폰 게임을 만들었다. 
# 게임에는 총 N개의 레벨이 있고, 각 레벨을 클리어할 때 마다 점수가 주어진다. 
# 플레이어의 점수는 레벨을 클리어하면서 얻은 점수의 합으로, 이 점수를 바탕으로 온라인 순위를 매긴다. 
# 동준이는 레벨을 난이도 순으로 배치했다. 하지만, 실수로 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우를 만들었다.

# 이 문제를 해결하기 위해 동준이는 특정 레벨의 점수를 감소시키려고 한다. 
# 이렇게해서 각 레벨을 클리어할 때 주는 점수가 증가하게 만들려고 한다.

# 각 레벨을 클리어할 때 얻는 점수가 주어졌을 때, 몇 번 감소시키면 되는지 구하는 프로그램을 작성하시오. 
# 점수는 항상 양수이어야 하고, 1만큼 감소시키는 것이 1번이다. 
# 항상 답이 존재하는 경우만 주어진다. 정답이 여러 가지인 경우에는 점수를 내리는 것을 최소한으로 하는 방법을 찾아야 한다.

N = int(input())

level_scores = []
for i in range(N):
    level_scores.append(int(input()))

decrease_amount = 0

# 뒤에서 두번째에서 부터 하나씩 앞으로 가면서 확인
for i in range(N - 2, -1, -1): 
    if level_scores[i] >= level_scores[i + 1]: # 뒤의 값보다 크거나 같다면
        decrease_amount += level_scores[i] - (level_scores[i + 1] - 1) # 현재 값에서 뒤의값의-1 값이되도록 감소
        level_scores[i] = level_scores[i + 1] - 1 # 다음 반복의 뒤의값이 될 값 업데이트

print(decrease_amount)


# 풀이
# 무엇 선택? 각 레벨의 보상을 몇으로 할지 선택
# 어떤 순서 선택? 높은 레벨 부터 보상값 선택
N = int(input())
L = [0] * N

for i in range(N):
    L[i] = int(input())

count = 0
for i in range(N - 2, -1, -1):
    if L[i] >= L[i + 1]:
        count += L[i] - (L[i+1] - 1)
        L[i] = L[i+1] - 1

print(count)