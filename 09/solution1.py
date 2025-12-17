from tqdm import tqdm


def read_input(fpath: str) -> list[tuple[int, int]]:
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    data = []
    for line in lines:
        data.append(tuple([int(idx) for idx in line.split(",")]))

    return data


def solve(data: list[tuple[int, int]]) -> int:
    max_area = 0
    for c0 in tqdm(data, ascii=True):
        for c1 in data:
            width = max(c0[0], c1[0]) - min(c0[0], c1[0]) + 1
            height = max(c0[1], c1[1]) - min(c0[1], c1[1]) + 1
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
