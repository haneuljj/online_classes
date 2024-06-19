# 실습문제 5.2.2
# 턱걸이 평균 측정 프로그램
# 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장 후, 리스트에 저장된 데이터의 평균을 구해 출력

week_exercise = []
num = 1

while num <= 7:
    week_exercise.append(int(input(str(num)+"일차 턱걸이 횟수>>>")))
    num += 1

print(week_exercise)

avg = sum(week_exercise) / len(week_exercise)
print(int(avg))