import re


def replace_donts(line: str) -> str:
    while "don't()" in line:
        dont = line.find("don't()")
        do = line.find("do()", dont)
        if dont != -1 and do != -1:
            line = line[:dont] + line[do + 4 :]
            print(dont, line[dont - 6 : dont + 6], do, line[do - 4 : do + 4])
    return line


def get_mulls_form_input(file_path: str) -> list[str]:
    occurances = []

    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            cleaned_line = replace_donts(line)
            occurances.extend(re.findall(r"mul\(\d+,\d+\)", cleaned_line))

    return occurances


def calc_mull(mull: str) -> int:
    mull = mull[4:-1]
    a, b = mull.split(",")
    return int(a) * int(b)


def sum_all_mulls(file_path: str) -> int:
    occurances = get_mulls_form_input(file_path)
    mulls = [calc_mull(mull) for mull in occurances]
    return sum(mulls)


if __name__ == '__main__':
    res = sum_all_mulls("day3/input.txt")
    print(res, "- sum of all of the results of just the enabled multiplications.")  # 173517243
