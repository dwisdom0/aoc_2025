def read_input(fpath: str) -> list[list[int]]:
    with open(fpath, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    data = []
    for line in lines:
        row = []
        for char in line:
            if char == ".":
                row.append(0)
            elif char == "@":
                row.append(1)
            else:
                raise ValueError(f"unexpected character in input: {char}")
        data.append(row)

    return data


def get_neighbor_coords(
    warehouse: list[list[int]], r: int, c: int
) -> list[tuple[int, int]]:
    potential_coords = [
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c + 1),
        (r + 1, c + 1),
        (r + 1, c),
        (r + 1, c - 1),
        (r, c - 1),
    ]
    coords = []
    for i, j in potential_coords:
        if i < 0 or i > len(warehouse) - 1:
            continue
        if j < 0 or j > len(warehouse[0]) - 1:
            continue
        coords.append((i, j))

    return coords


def solve(warehouse: list[list[int]]) -> int:
    accessible = 0
    for r, row in enumerate(warehouse):
        for c, val in enumerate(row):
            if val == 0:
                continue
            neighbor_sum = 0
            for nr, nc in get_neighbor_coords(warehouse, r, c):
                neighbor_sum += warehouse[nr][nc]
            if neighbor_sum < 4:
                accessible += 1
    return accessible


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
