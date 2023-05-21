import sys
input = sys.stdin.readline

word = 1

while (word != 0):
    word = int(input())
    str_word = str(word)[::-1]
    if str(word) == str_word:
        print('yes')
    else:
        print('no')