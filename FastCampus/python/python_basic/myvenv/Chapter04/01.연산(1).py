# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# - 문자열연산
tag1 = "#내꺼하자"
tag2 = "#오늘부터1일"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3
print(tag)

message = "우린 모두 파이썬을 사랑합니다.\n" * 5
print(message)

# 복합할당연산자
level = 10
level += 1 # level = level + 1

health = 2000
health -= 300

attack = 300
attack *= 1.5

speed = 420
speed /= 2

print(level, health, attack, speed)