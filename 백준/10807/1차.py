count = 0

# 입력할 숫자의 개수
n = int(input())

# n값 만큼 숫자 입력하기 - 파이썬에서는 n만큼 입력받는 조건을 만족시키지 않아도 됨
arr = list(map(int, input().split()))

# 찾을 숫자 입력
v = int(input())

print(arr.count(v))  # count 함수가 있다는 사실 잊지 말기
