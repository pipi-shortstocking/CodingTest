import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    age, name = map(str, input().rstrip().split())
    age_int = int(age)
    arr.append((age_int, name))

arr.sort(key=lambda arr: int(arr[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
