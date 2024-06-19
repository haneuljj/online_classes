# 실습문제 5.1.4
# 프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다
# 세과목의 평균점수가 80점 이상이면 합격이어야하는데 오류 발생해서 80점이상일 경우 불합격이 표시되도록 프로그램 작성
# 0에서 100사이의 숫자를 입력하지 않으면 "잘못 입력하였습니다" 출력

kor = int(input("국어>>> "))
math = int(input("수학>>> "))
eng = int(input("영어>>> "))

avg = (kor + math + eng) / 3

# if 0 <= kor <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
    # if avg >= 80:
    #   print("불합격") ...
# else:
    # print("잘못 입력하였습니다.")
if (kor<0 or kor>100) or (math<0 or math>100) or (eng<0 or eng>100):
    print("잘못 입력하였습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")
