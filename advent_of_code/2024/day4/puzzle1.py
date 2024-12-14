def read_input(file_path: str) -> list[str]:
    result = []
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            result.append(stripped_line)
    return result


def count_xmas(grid):
    word = "XMAS"
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Directions: (delta_row, delta_col)
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right
        (-1, -1),  # up-left
        (1, -1),  # down-left
        (-1, 1),  # up-right
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(
                    is_valid(r + dr * i, c + dc * i) and grid[r + dr * i][c + dc * i] == word[i]
                    for i in range(word_length)
                ):
                    count += 1

    return count


if __name__ == '__main__':
    grid = read_input("day4/input.txt")
    res = count_xmas(grid)
    print(res)  # 2504
