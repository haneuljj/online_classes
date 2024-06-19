# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

remainder_numbers = []
for i in range(10):
    n = int(input())
    remainder_numbers.append(n % 42)

answer = []
remainder_numbers.sort()
answer.append(remainder_numbers[0])
for i in range(1, 10):
    if(remainder_numbers[i] != remainder_numbers[i - 1]):
        answer.append(remainder_numbers[i])

print(len(answer))


# 체크배열 사용
check = [0] * 42

for i in range(10):
    n = int(input())
    check[n % 42] = 1

sum = 0
for i in range(42):
    sum += check[i]

print(sum)