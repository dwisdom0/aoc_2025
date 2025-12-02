def read_input(fpath: str) -> list[tuple[str, int]]:
    lines = []
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    data = []
    for line in lines:
        data.append((line[0], int(line[1:])))
    return data


def rotate(dial: int, direction: str, amount: int) -> int:
    # python handle negative modulos the way I want for this
    if direction == "L":
        return (dial - amount) % 100
    return (dial + amount) % 100


if __name__ == "__main__":
    data = read_input("input.txt")
    dial = 50
    num_zeros = 0
    for op in data:
        dial = rotate(dial, *op)
        if dial == 0:
            num_zeros += 1
    print(num_zeros)
