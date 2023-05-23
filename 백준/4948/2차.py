import sys, math

input = sys.stdin.readline


def pri(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True


limit = list(range(2, 246912))  # 문제에서 제한한 범위
arr = []

for i in limit:
    if pri(i):  # 범위 안에서 소수인 값 모두 추가 해놓음
        arr.append(i)

while True:
    cnt = 0
    n = int(input())

    if n == 0:
        break

    for i in arr:
        if n < i <= 2 * n:  # 입력한 값의 범위에 i가 있으면 카운팅 수 증가
            cnt += 1
    print(cnt)
