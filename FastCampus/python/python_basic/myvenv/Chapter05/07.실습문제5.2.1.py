# 실습문제 5.2.1
# 1번부터 5번까지의 1분간 팔굽혀펴기의 개수이다
result = [33, 40, 12, 63, 52]

# 문항1 : 6번의 팔굽혀펴기 개수 9를 마지막에 추가
result.append(9)
print(result)

# 문항2 : 2번의 재측정 개수가 50. 변경
result[1] = 50
print(result)

# 문항3 : 3번부터 6번까지 데이터 슬라이싱
print(result[2:])

# 문항 4: 모든 데이터를 오름차순으로 정렬
result.sort()
print(result)
