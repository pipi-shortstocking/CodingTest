import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sen = str(input().rstrip())
    answer = ""
    start = 0
    word = ""

    # word += sen[::-1]
    # print(word)

    for i in range(len(sen)):
        if sen[i] == " " or i == len(sen) - 1:  # 공백이거나 문장의 끝일 때
            word = sen[start:i]
            if i == len(sen) - 1:  # 문장 끝일 때에는 끝 인덱스 설정 X
                word = sen[start:]

            answer += word[::-1] + " "

            word = ""
            start = i + 1
    # answer = answer[: len(answer) - 1] 굳이 필요 없음을 확인함
    print(answer)
    # print(list(answer))

# word += str(t)
# print(word)
