n, m = map(int, input().split())
n_min = list()

for i in range(n):
    n_list = list(map(int, input().split()))
    n_min.append(min(n_list))

print(max(n_min))
