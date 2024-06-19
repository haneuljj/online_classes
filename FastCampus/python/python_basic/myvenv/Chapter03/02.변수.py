# 변수 : 데이터가 들어있는 공간, 새로운 데이터를 계속 할당 가능
# 변수이름 = 데이터
# =: 할당 연산자 - 오른쪽의 데이터를 왼쪽의 변수에 저장

# 변수 이름짓기
# - 데이터를 표현할 수 있는 이름으로 짓기
# - 문자부터 시작
# - 대소문자 구분
# - _로 시작 가능
# - 예약된 키워드는 사용불가


# 마스터이 챔피언 데이터를 변수에 저장
name = "마스터이"
level = 5
health = 800
attack = 90
print(name, level, health, attack)

# 변수에 저장된 데이터를 변경
level = level + 1
health = health + 50
attack = attack + 10
print(name, level, health, attack)