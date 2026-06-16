def solution(s):
    answer = ""
    temp = ""

    # words에서 해당하는 단어를 찾으면 그 인덱스 값이 숫자가 됨
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for c in s:
        if c.isdigit():
            answer += c
        else:
            temp += c

            if temp in words:
                idx = words.index(temp)
                answer += str(idx)
                temp = ""

    return int(answer)

# s = "one4seveneight"
# s = "23four5six7"
# s = "2three45sixseven"
s = "123"

print(solution(s))