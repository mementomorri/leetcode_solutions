import re


def replace_until(text, start_word, end_word, replacement):
    start_index = text.find(start_word)
    end_index = text.find(end_word, start_index)

    if start_index != -1 and end_index != -1:
        return text[:start_index] + replacement + text[end_index:]
    else:
        return text


def replace_until_pair(text, start_word, end_word, replacement):
    pattern = re.escape(start_word) + r'.*?' + re.escape(end_word)
    new_text = re.sub(
        pattern,
        replacement,
        text,
    )

    while new_text != text:
        text = new_text
        new_text = re.sub(pattern, replacement, text)

    final_pattern = re.escape(start_word) + r'.*?$'
    new_text = re.sub(final_pattern, '', text)

    return new_text


def replace_donts(line: str) -> str:
    return replace_until_pair(line, "don't()", "do()", "")


def get_mulls_form_input(file_path: str) -> list[str]:
    occurences = []

    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            cleaned_line = replace_donts(line)
            occurences.extend(re.findall(r"mul\(\d+,\d+\)", cleaned_line))

    return occurences


def calc_mull(mull: str) -> int:
    mull = mull[4:-1]
    a, b = mull.split(",")
    return int(a) * int(b)


def sum_all_mulls(file_path: str) -> int:
    occurences = get_mulls_form_input(file_path)
    mulls = [calc_mull(mull) for mull in occurences]
    return sum(mulls)


if __name__ == '__main__':
    res = sum_all_mulls("day3/input.txt")
    print(res, "- sum of all of the results of just the enabled multiplications.")  # 102 360 389
