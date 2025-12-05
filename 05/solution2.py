from collections import defaultdict
from copy import deepcopy


def read_input(fpath: str) -> list[tuple[int, int]]:
    with open(fpath, "r") as f:
        chars = f.read()
    ranges_chunk, _ = chars.split("\n\n")

    parsed_ranges = []
    for r in ranges_chunk.split("\n"):
        start, stop = r.strip().split("-")
        parsed_ranges.append((int(start), int(stop)))

    return parsed_ranges


def find_overlaps(
    ranges: list[tuple[int, int]],
) -> dict[tuple[int, int], list[tuple[int, int]]]:
    # there's probably a better way to do this that's not O(n^2)
    # I don't really want to figure out how to sort ranges though
    # probably insert each endpoint into a balanced tree
    # where each node is a range spanning all child ranges
    # and then if the two endpoints end up in different leaves, you can merge those
    # and then the leaves will be the merged ranges
    # somthing like that idk
    overlaps = defaultdict(list)
    for r0 in ranges:
        for r1 in ranges:
            if r0 == r1:
                continue
            # |--------|
            #    |-------|
            if r0[0] <= r1[0] and r1[0] <= r0[1]:
                overlaps[r0].append(r1)
            #     |--------|
            #  |-------|
            elif r1[0] <= r0[0] and r0[0] < r1[1]:
                overlaps[r0].append(r1)
            # sometimes a range is only 1 number
            #  |
            #  |-----|
            elif r0[0] == r0[1] and (r0[0] == r1[0] or r0[0] == r1[1]):
                overlaps[r0].append(r1)

    return overlaps


def merge_ranges(
    ranges: list[tuple[int, int]], debug: bool = False
) -> list[tuple[int, int]]:
    overlaps = find_overlaps(ranges)
    if debug:
        print(f"{ranges=}")
        print(f"{overlaps=}")
    old_ranges = deepcopy(ranges)
    while len(overlaps) > 0:
        new_ranges = []
        for r in old_ranges:
            if r not in overlaps:
                new_ranges.append(r)
                continue
            lower = min(r[0], min([x[0] for x in overlaps[r]]))
            upper = max(r[1], max([x[1] for x in overlaps[r]]))
            if debug:
                print(f"{r} -> {(lower, upper)}")
            new_ranges.append((lower, upper))

        new_ranges = list(set(new_ranges))
        overlaps = find_overlaps(new_ranges)
        if debug:
            print(f"{new_ranges=}")
            print(f"{overlaps=}")
        old_ranges = deepcopy(new_ranges)

    return old_ranges


def solve(ranges: list[tuple[int, int]]) -> int:
    ranges = merge_ranges(ranges)
    fresh = 0
    for r in ranges:
        fresh += r[1] - r[0]
        fresh += 1
    return fresh


def main():
    parsed_ranges = read_input("input.txt")
    print(solve(parsed_ranges))


if __name__ == "__main__":
    main()
