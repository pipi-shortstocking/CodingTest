N, M, K = map(int, input().split())
data = list(map(int, input().split()))
a = 0
count = 0

data.sort()
# print(data)

while count < M:
    for i in range(0, K):
        a += data[N-1]
        count += 1
        #print("f :", a)
        #print("count:", count)

    a += data[N-2]
    count += 1
    # print(a)
    #print("count:", count)

print(a)
