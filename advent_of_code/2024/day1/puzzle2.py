import csv
import collections


def find_similarity_score(csv_path: str) -> int:
    total = 0
    left, right = [], []

    with open(csv_path) as file:
        input_csv = csv.DictReader(file)
        for line in input_csv:
            left.append(int(line['left']))
            right.append(int(line['right']))

    right = collections.Counter(right)
    total = sum([n * right[n] for n in left])
    return total


if __name__ == '__main__':
    res = find_similarity_score("day1/input.csv")
    print("lists similarity:", res)
