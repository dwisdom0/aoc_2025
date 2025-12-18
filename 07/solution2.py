def read_input(fpath: str) -> list[str]:
    with open(fpath, "r") as f:
        lines = f.readlines()

    data = [line.strip() for line in lines]
    return data


def solve(manifold: list[str]) -> int:
    # TODO: this hangs
    # might have to detect cycles or do a dynamic programming
    # like bottom-up thing
    start_col = manifold[0].index("S")

    beams = []
    beams.append((0, start_col))

    completed_beams = 0

    while len(beams):
        if len(beams) == 0:
            break
        beam_pos = beams.pop(-1)
        new_row = beam_pos[0] + 1
        col = beam_pos[1]

        # if we hit the bottom, this timeline is done
        if new_row == len(manifold) - 1:
            completed_beams += 1
            continue

        # if we hit a splitter, this beam is done
        # and we have to start two new beams
        if manifold[new_row][col] == "^":
            beams.append((new_row, col - 1))
            beams.append((new_row, col + 1))

        # if we didn't hit a splitter, continue searching downward
        else:
            beams.append((new_row, col))

    return completed_beams


def main():
    # it works correctly for the test input
    # but it hangs on the real input
    # so I probably have to detect cycles or something?
    # I'm not sure how a cycle would even happen though
    # since it's always going down
    # maybe it's like fib where it's just repeating a ton of work
    # once it gets near the bottom
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
