word = str(input())
r = ""

for i in range(len(word)):
    if word[i].isupper() is True:
        r += word[i].lower()
    if word[i].islower() is True:
        r += word[i].upper()

print(r)
