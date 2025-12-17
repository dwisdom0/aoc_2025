def read_input(fpath: str) -> list[list]:
    with open(fpath, "r") as f:
        lines = f.readlines()

    # some numbers are left-aligned
    # others are right-aligned
    # so we need to build a grid for each problem
    # based on the position of the operator
    # the operator is the left-most column
    # the next operator -2 is the right-most column
    # 123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +

    # read the indices from the last line of operators
    op_line = lines.pop(-1)

    op_idxs = []
    ops = []
    for i, op in enumerate(op_line):
        if op == "+" or op == "*":
            op_idxs.append(i)
            ops.append(op)

    op_idx_pairs = []
    for i, op_idx in enumerate(op_idxs[:-1]):
        if i == len(op_idxs) - 1:
            break
        # -1 because python slice syntax doesn't include the ending index
        # and we need to go up to -2
        op_idx_pairs.append((op_idx, op_idxs[i + 1] - 1))
    op_idx_pairs.append((op_idxs[-1], len(op_line)))

    padded_num_lists = []
    for _ in range(len(op_idxs)):
        padded_num_lists.append(list())

    for line in lines:
        for i, pair in enumerate(op_idx_pairs):
            padded_num_lists[i].append(line[pair[0] : pair[1]].rstrip("\n"))

    problems = []
    for _ in range(len(op_idxs)):
        problems.append(list())

    for problem_idx, padded_nums in enumerate(padded_num_lists):
        for col_idx in range(len(padded_nums[0])):
            num = ""
            for padded_num in padded_nums:
                digit = padded_num[col_idx]
                if digit != " ":
                    num += digit

            problems[problem_idx].append(int(num))

    for problem_idx, op in enumerate(ops):
        problems[problem_idx].insert(0, op)

    return problems


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
