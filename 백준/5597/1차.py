# 1에서 30까지의 수를 담고 있는 리스트 생성
arr = [i for i in range(1, 31)]

# 입력 받은 숫자를 리스트에서 제거하기
for _ in range(28):
    num = int(input())
    arr.remove(num)

# 리스트 안에서 가장 작은 수, 가장 큰 수 순서로 출력하기
print(min(arr))
print(max(arr))
