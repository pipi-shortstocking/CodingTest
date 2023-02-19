t = int(input())
r = ""

for _ in range(t):
    word = str(input())
    final = len(word)

    r += word[0]
    r += word[final-1]

    print(r)
    r = ""
