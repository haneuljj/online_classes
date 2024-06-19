# 실습문제 5.3.1
# 구구단 출력 프로그램

dan = int(input("몇 단을 출력할까요?>>> "))

for i in range(1, 10):
    print(dan, "*", i, "=", dan*i)
