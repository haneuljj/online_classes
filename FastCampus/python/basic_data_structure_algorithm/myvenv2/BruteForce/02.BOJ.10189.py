# N개의 정수로 이루어진 배열 A가 주어진다. 
# 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 주어진 배열의 숫자들에서 2개씩 뽑아서 차의 절댓값을 구한후
# 최댓값을 얻을 수 있는 숫자들의 순서(차의 절댓값의 조합) 구하기

from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))

# 풀이
# 모든 가능한 순서의 배열을 다 실험, 차이의 합을 하나씩 해보고 최댓값 찾기
max = 0
for a in list(permutations(numbers, N)):
    sum = 0
    for i in range(N - 1):
        sum += abs(a[i] - a[i+1])
    if max < sum:
        max = sum

print(max) 