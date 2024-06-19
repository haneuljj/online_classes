# 실습문제 6.1.1
# docstring: 설명문
def multiply(x, y):
    """
    두 수의 곱셈 결과를 반환하는 함수
    매개변수x : 숫자
    매개변수y : 숫자
    """
    result = x* y
    return result 

# 실습문제 6.1.2
# 세개의 정수를 인자로 받아 합계와 평균을 출력해주는 함수 정의
def printSumAvg(x, y, z):
    """
    세 개의 숫자를 받아 합계와 평균을 출력하는 함수
    """
    sum = x + y + z
    avg = sum / 3
    print(f"합계: {sum}  평균: {avg}")

printSumAvg(10, 20, 30)