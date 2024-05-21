n = int(input())


def draw(len):
    if len == 1:
        return ["*"]

    if len >= 6:
        n = len // 2
    else:
        n = len // 3

    stars = draw(n)  # 수정
    arr = []

    for s in stars:
        arr.append(" " * (len - 1) + s + " " * (len - 1))
    for s in stars:
        arr.append(" " + s + " " + s + " ")
    for s in stars:
        arr.append(s * 5)
    return arr


print("\n".join(draw(n)))
