N, M, K = map(int, input().split())
data = list(map(int, input().split()))
result = 0
count = 0

data.sort()
# print(data)

while count < M:
    for i in range(0, K):
        result += data[N-1]
        count += 1
        #print("f :", result)
        #print("count:", count)

    result += data[N-2]
    count += 1
    # print(result)
    #print("count:", count)

print(result)
