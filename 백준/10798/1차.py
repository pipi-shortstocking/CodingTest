arr = [[0]*5 for _ in range(5)]
# word = [0]*5
word = []
length = [0]*5

# print(arr)
# print(word)

for i in range(5):
    arr[i] = str(input())
    length[i] = len(arr[i])

# print(length)
# print(arr)

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            word.append(arr[j][i])
            #word[i] += arr[j][i]

for i in word:
    print(i, end='')
