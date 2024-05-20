n = int(input())


def star(len):
    if len == 1:
        return ["*"]

    stars = star(len // 3)
    arr = []

    for s in stars:
        arr.append(s * 3)
    for s in stars:
        arr.append(s + " " * (len // 3) + s)
    for s in stars:
        arr.append(s * 3)
    return arr


print("\n".join(star(n)))
