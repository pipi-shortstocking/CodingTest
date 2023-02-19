word = str(input())

for i in range(len(word)):
    if word[i].isupper() is True:
        word[i].lower()
    if word[i].islower() is True:
        word[i].upper()

print(word)
