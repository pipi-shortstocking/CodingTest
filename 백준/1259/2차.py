import sys
input = sys.stdin.readline

while (True):
    word = int(input())
    str_word = str(word)[::-1]
    if (word == 0):
        break 
    elif str(word) == str_word:
        print('yes')
    else:
        print('no')