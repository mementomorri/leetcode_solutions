def addSpaces(s: str, spaces: list[int]) -> str:
    i, j = 0, 0
    res = []

    while i < len(s) and j < len(spaces):
        if i < spaces[j]:
            res.append(s[i])
            i += 1
        else:
            res.append(" ")
            j += 1

    if i < len(s):
        res.append(s[i:])

    return "".join(res)


if __name__ == '__main__':
    print(addSpaces("EnjoyYourCoffee", [5, 9]))
    print(addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))
