def read_input(fpath: str) -> list[tuple[str, int]]:
    lines = []
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    data = []
    for line in lines:
        data.append((line[0], int(line[1:])))
    return data


def rotate(dial: int, direction: str, amount: int) -> tuple[int, int]:
    new_dial = None
    zeros = 0
    if direction == "L":
        # python handle negative modulos the way I want for this
        new_dial = (dial - amount) % 100

        if dial - amount < 0:
            zeros += abs((dial - amount) // 100)
            # if we started at 0, we shouldn't count that again
            if dial == 0:
                zeros -= 1

        if new_dial == 0:
            zeros += 1

    else:
        new_dial = (dial + amount) % 100

        if dial + amount >= 100:
            zeros += (dial + amount) // 100

    return new_dial, zeros


if __name__ == "__main__":
    data = read_input("input.txt")
    dial = 50
    num_zeros = 0
    for op in data:
        # print(f'\n{dial=}')
        dial, zeros = rotate(dial, *op)
        # print(f'{dial=}')
        num_zeros += zeros
        # print(f'{num_zeros=}')
    print(num_zeros)
