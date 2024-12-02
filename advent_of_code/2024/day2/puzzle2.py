import csv


def count_safe_reps(csv_path: str) -> int:
    total = 0
    with open(csv_path) as file:
        input_csv = csv.reader(file, delimiter=" ")
        for line in input_csv:
            row = [int(n) for n in line]
            errs = 0
            asc_ord = False if row[0] > row[1] > row[2] else True
            for i in range(1, len(row)):
                if abs(row[i - 1] - row[i]) > 3 or abs(row[i - 1] - row[i]) == 0:
                    errs += 1
                    continue
                if asc_ord and row[i] - row[i - 1] < 0:
                    errs += 1
                    continue
                if not asc_ord and row[i - 1] - row[i] < 0:
                    errs += 1
                    continue
            if errs < 2:
                total += 1
    return total


if __name__ == '__main__':
    res = count_safe_reps("day2/input.csv")
    print(res, "- reports are safe, glad to problem demper.")  # 455
