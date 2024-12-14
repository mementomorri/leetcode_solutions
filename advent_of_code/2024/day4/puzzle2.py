def read_input(file_path: str) -> list[str]:
    result = []
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            result.append(stripped_line)
    return result


def count_x_mas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(1, rows - 1):  # Start from 1 to avoid out-of-bounds
        for c in range(1, cols - 1):  # Start from 1 to avoid out-of-bounds
            # Check for the "X-MAS" pattern
            if (
                grid[r - 1][c - 1] == 'M'
                and grid[r - 1][c + 1] == 'S'
                and grid[r][c] == 'A'
                and grid[r + 1][c - 1] == 'M'
                and grid[r + 1][c + 1] == 'S'
            ):
                count += 1

            # Check for the reverse "X-MAS" pattern
            if (
                grid[r - 1][c - 1] == 'M'
                and grid[r - 1][c + 1] == 'S'
                and grid[r][c] == 'A'
                and grid[r + 1][c - 1] == 'S'
                and grid[r + 1][c + 1] == 'M'
            ):
                count += 1

    return count


if __name__ == '__main__':
    grid = read_input("day4/input.txt")
    res = count_x_mas(grid)
    print(res)  # 537?
