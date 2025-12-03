from itertools import batched


def read_input(fpath: str) -> list[tuple[int, int]]:
    data = []
    with open(fpath, "r") as f:
        lines = f.readlines()
        lines = lines[0].strip().split(",")
    for line in lines:
        start, end = line.split("-")
        data.append((int(start), int(end)))

    return data


def is_repeat(num: int):
    str_num = str(num)

    for batch_size in range(1, (len(str_num) // 2) + 1):
        if len(str_num) % batch_size != 0:
            continue

        batches = set([tuple(b) for b in batched(str_num, batch_size)])
        if len(batches) == 1:
            return True
    return False


def solve(data: list[tuple[int, int]]):
    repeats = []
    for start, stop in data:
        for i in range(start, stop + 1):
            if is_repeat(i):
                repeats.append(i)

    return sum(repeats)


if __name__ == "__main__":
    data = read_input("input.txt")
    print(solve(data))
