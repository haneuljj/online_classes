# 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 
# 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 
# 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.
# 그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 
# A는 결코 선발되지 않는다.

# 이러한 조건을 만족시키면서, 
# 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    total_score = []  # 서류, 면접 모두 담을 리스트

    # 각 지원자의 점수를 총 리스트에 넣기
    for _ in range(N):
        score = list(map(int, input().split()))
        total_score.append(score)

    # 첫번째 열 기준으로 정렬하기
    total_score.sort()
    
    #### 비교대상의 값 앞의 모든 값을 비교할 필요x -> 모두 비교하면 시간복잡도가 똑같이 O(N^) -> 비효율
    #### 앞의 애들에서 최고성적을 갱신하여 그거보다 작은지를 확인 -> 시간복잡도 O(N)

    # 첫 번째 지원자는 무조건 선발
    result = 1
    best_interview_score = total_score[0][1]

    # 두번째 지원자부터 비교
    for i in range(1, N):
        if total_score[i][1] < best_interview_score:  # 앞의 값보다 작으면
            result += 1
            best_interview_score = total_score[i][1]  # 앞의 애들의 최고 면접 성적 갱신

    print(result)
