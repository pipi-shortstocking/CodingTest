N, M, K = map(int, input().split())
# N : 배열의 수
# M : 더해지는 횟수
# K : 최대 횟수
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

count = int(M/(K+1))*K + M % (K+1)  # 큰 수가 더해지는 횟수

result = 0
result += count * first  # 가장 큰 수 더하기

# 전체 더해지는 횟수에서 큰 수가 더해지는 횟수를 빼면 나머지 횟수가 되는 것은 자명한 사실
result += (M-count) * second  # 두번째로 큰 수 더하기

print(result)
