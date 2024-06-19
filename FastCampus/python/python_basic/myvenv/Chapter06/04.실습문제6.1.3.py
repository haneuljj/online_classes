# 실습문제 6.1.3
# 로또 예상번호 추출 프로그램 작성
# 1. 로또 번호 6개 생성
# 2. 로또 번호는 1~45 까지의 랜덤한 번호
# 3. 6개의 숫자 모두 달라야함
import random

def get_random_number():
    number = random.randint(1, 45)
    return number

def get_lotto_numbers():
    number_list = []
    while len(number_list) != 6:
        current_num = get_random_number()

        if current_num not in number_list: # **멤버십연산자**
            number_list.append(current_num)

    number_list.sort()
    for num in number_list:
        print(num, end=" ")

get_lotto_numbers()



