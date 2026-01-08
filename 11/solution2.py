

def read_input(fpath: str) -> dict[str, list[str]]:
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    data = {}
    for line in lines:
        machine, output_str = line.split(": ")
        outputs = output_str.split(" ")
        data[machine] = list(outputs)

    return data


def solve(data: dict[str, list[str]]) -> int:
    # hangs just counting paths from svr -> out
    # so might have to detect cycles or something
    # stack = ["svr"]
    # num_out = 0
    # while len(stack):
    #     machine = stack.pop(-1)
    #     if machine == "out":
    #         num_out += 1
    #         continue
    #     for neighbor in data[machine]:
    #         stack.append(neighbor)
    # return num_out

    stack = [("svr", ["svr"])]
    out_paths = []
    while len(stack):
        machine, path = stack.pop(-1)
        if machine == "out":
            out_paths.append(path[:])
            continue
        for neighbor in data[machine]:
            stack.append((neighbor, path[:] + [neighbor]))

    num_valid = 0
    for out_path in out_paths:
        if "fft" in out_path and "dac" in out_path:
            num_valid += 1

    return num_valid


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
