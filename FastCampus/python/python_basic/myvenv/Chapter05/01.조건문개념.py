# 조건문
# : 조건에 따라 실행할 명령이 달라지는것

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>> ")

if input_pass == origin_pass: # 조건A
    # 조건A가 참이라면
    print("로그인 성공!")
    print("반갑습니다!")
elif input_pass == "": # 조건B
    # 조건 A 거짓, 조건 B 참
    print("아무것도 입력하지 않았습니다!")
else:
    # 조건A가 거짓이라면
    print("로그인 실패!")
    print("비밀번호를 확인하세요!")


