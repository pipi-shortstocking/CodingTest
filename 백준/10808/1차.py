import sys
input = sys.stdin.readline

s = str(input().rstrip())
# print(s, ord(s))

alphabet = [0] * 26
for i in s:
    # alphabet[int(ord(i)%97)] += 1
    alphabet[ord(i)-97] += 1

for i in alphabet:
    print(i, end= " ")
print()