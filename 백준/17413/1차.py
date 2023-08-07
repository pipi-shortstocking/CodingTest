import sys

input = sys.stdin.readline

sen = input().rstrip()
arr = []

if sen.find("<") != -1:
    # # print("yes it is")
    # for i in range(len(sen)):
    #     if sen[i] == ">":
    #         arr.append(i + 1)
    #     if sen[i] == "<":
    #         arr.append(i)
    # # print(arr)
    # # print(sen[6:9])
else:
    # print("no here not")
    sen = sen.split()

    for word in sen:
        print(word[::-1], end=" ")


# # arr = [1, 2, 3, 4, 5, 6]
# # arr[:3] = [3, 2, 1]

# # print(arr)