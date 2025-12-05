def read_input(fpath: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(fpath, "r") as f:
        chars = f.read()
    ranges_chunk, ids_chunk = chars.split("\n\n")

    parsed_ranges = []
    for r in ranges_chunk.split("\n"):
        start, stop = r.strip().split("-")
        parsed_ranges.append((int(start), int(stop)))

    ids = []
    for _id in ids_chunk.strip().split("\n"):
        ids.append(int(_id.strip()))

    return parsed_ranges, ids


def solve(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    fresh = 0
    for i in ids:
        for r in ranges:
            if r[0] <= i and i <= r[1]:
                fresh += 1
                break
    return fresh


def main():
    parsed_ranges, ids = read_input("input.txt")
    print(solve(parsed_ranges, ids))


if __name__ == "__main__":
    main()
