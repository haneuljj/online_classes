# 실습문제 5.3.3
# 1. 연습할 한국어가 담긴 리스트를 만든다
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료.

kor_words = ["사랑해", "귀엽다", "고마워", "행복해"]

print("Let's Learning Korean")

correct_answer = 0

for word in kor_words:
    print(word)
    input_word = input()

    if input_word == word:
        correct_answer += 1

print("전체 문제 개수: ", len(kor_words), "개")
print("맞힌 문제 개수: ", correct_answer, "개")
print("틀린 문제 개수: ", len(kor_words) - correct_answer, "개")
