def read_input(fpath: str) -> list[list]:
    with open(fpath, "r") as f:
        lines = f.readlines()

    # the final line is the list of operations
    ops = lines.pop(-1).strip().split()

    # have to transpose to get the columns instead of the rows
    num_problems = len(lines[0].strip().split())
    data = []
    for n in range(num_problems):
        data.append(list())

    for line in lines:
        nums = line.strip().split()
        for i, num in enumerate(nums):
            data[i].append(int(num))

    for i, op in enumerate(ops):
        data[i].insert(0, op)

    return data


def solve(problems: list[list]) -> int:
    total = 0

    for problem in problems:
        op = problem.pop(0)
        if op == "+":
            total += sum(problem)
        elif op == "*":
            problem_total = 1
            for num in problem:
                problem_total *= num
            total += problem_total
        else:
            raise ValueError(f"Unsupported operation: {op}")
    return total


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
