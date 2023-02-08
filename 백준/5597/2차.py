# 28개의 숫자 입력 받기
arr = [int(input()) for i in range(28)]

# 1부터 30까지의 수 중에서 없는 숫자  출력하기
for i in range(1, 31):
    if i not in arr:
        print(i)
