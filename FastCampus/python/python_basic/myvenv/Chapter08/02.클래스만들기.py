class Monster:
    def say(self):
        print("나는 몬스터다!")

goblin = Monster()  # 인스턴스 생성
goblin.say()  # 메서드 호출


# 파이썬에서는 자료형도 클래스
a = 10
b = "문자열 객체"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__()) # 문자열에 있는 메서드 리스트 확인