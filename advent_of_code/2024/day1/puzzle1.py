import csv


def find_total_distance(csv_path: str) -> int:
    total = 0
    left, right = [], []

    with open(csv_path) as file:
        input_csv = csv.DictReader(file)
        for line in input_csv:
            left.append(line['left'])
            right.append(line['right'])

    left.sort(reverse=True)
    right.sort(reverse=True)
    while left and right:
        curr_left = int(left.pop())
        curr_right = int(right.pop())
        total += abs(curr_left - curr_right)

    return total


if __name__ == '__main__':
    res = find_total_distance("day1/input.csv")
    print("total distace is:", res)
