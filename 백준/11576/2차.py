import sys

input = sys.stdin.readline

a, b = map(int, input().split())  # a: 미래 진법 b: 정이 진법
m = int(input())  # a진법으로 나타낸 숫자의 자리수의 개수
m_arr = list(
    map(int, input().split())
)  # a진법을 이루고 있는 숫자 m개를 높은 자리 수 부터 저장

# 출력 : m_arr에 있는 a진법 수를 b진법으로 변환하여 출력


# a 진법을 10진법으로 변경
ten = 0
i = 1
for num in m_arr:
    # print(num, a, (m - i))
    ten += num * (a ** (m - i))
    i += 1
    # print(ten)

# 10진법을 b 진법으로 변경
ans = []

while ten != 0:
    ans.append(ten % b)
    ten = ten // b
    # print(ans)

ans.reverse()
print(*ans)
