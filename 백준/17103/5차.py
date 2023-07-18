import sys, math

input = sys.stdin.readline

n = 1000000  # 2부터 n까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)]
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:  # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

t = int(input())

for _ in range(t):
    num = int(input())
    cnt = 0

    for k in range(2, num // 2 + 1):
        if array[k] and array[num - k]:
            cnt += 1

    print(cnt)
