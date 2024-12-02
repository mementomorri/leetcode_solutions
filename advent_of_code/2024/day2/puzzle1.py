import csv


def count_safe_reps(csv_path: str) -> int:
    total = 0
    with open(csv_path) as file:
        input_csv = csv.reader(file, delimiter=" ")
        for line in input_csv:
            row = [int(n) for n in line]
            if not (row == sorted(row) or row[::-1] == sorted(row)):
                continue
            for i in range(1, len(row)):
                if abs(row[i - 1] - row[i]) > 3 or abs(row[i - 1] - row[i]) == 0:
                    total -= 1
                    break
            total += 1
    return total


if __name__ == '__main__':
    res = count_safe_reps("day2/input.csv")
    print(res, "- reports are safe.")  # 402
