# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 
# 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 
# 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

attendence = []
for i in range(31): # 0번째 인덱스 사용 안함
    attendence.append(0)
# attendence = [0] * 31

for i in range(28):
    attend_num = int(input())
    attendence[attend_num] = 1

answer = []
for i in range(1, 31):
    if attendence[i] == 0:
        answer.append(i)

print(answer[0])
print(answer[1])