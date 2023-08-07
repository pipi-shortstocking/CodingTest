alphabat = "abcdefghijklmnopqrstuvwxyz"

s = str(input())

for i in range(len(alphabat)):
    print(s.find(alphabat[i]), end=" ")

for i in alphabat:
    print(s.find(i), end=" ")
