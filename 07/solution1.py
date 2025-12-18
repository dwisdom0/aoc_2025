from collections import deque


def read_input(fpath: str) -> list[str]:
    with open(fpath, "r") as f:
        lines = f.readlines()

    data = [line.strip() for line in lines]
    return data


def solve(manifold: list[str]) -> int:
    hit_splitters = set()
    start_idx = manifold[0].index("S")

    beams = deque()
    beams.append((0, start_idx))

    while len(beams):
        beam_pos = beams.pop()
        new_row = beam_pos[0] + 1
        col = beam_pos[1]

        # if we hit the bottom, this beam is done
        if new_row == len(manifold) - 1:
            continue

        # if we hit a splitter, this beam is done
        # and we have to start two new beams
        if manifold[new_row][col] == "^":
            if (new_row, col) in hit_splitters:
                continue
            hit_splitters.add((new_row, col))
            try:
                beams.append((new_row, col - 1))
            except IndexError:
                pass
            try:
                beams.append((new_row, col + 1))
            except IndexError:
                pass
        else:
            beams.append((new_row, col))

    return len(hit_splitters)


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
