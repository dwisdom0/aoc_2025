from copy import deepcopy


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
    stack = [("you", data["you"])]
    out_count = 0
    while len(stack):
        machine, path = stack.pop(-1)
        if machine == "out":
            out_count += 1
            continue
        for neighbor in data[machine]:
            stack.append((neighbor, deepcopy(path)))

    return out_count


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
