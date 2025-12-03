def read_input(fpath: str) -> list[list[int]]:
    with open(fpath, "r") as f:
        lines = f.readlines()
        lines = [list(line.strip()) for line in lines]

    data = []
    for line in lines:
        bank = []
        for char in line:
            bank.append(int(char))
        data.append(bank)
    return data


def get_joltage(bank: list[int]) -> int:
    # find the largest digit (not including the last one) in the bank
    max_d1 = 0
    max_d1_idx = 0
    for i, digit in enumerate(bank[:-1]):
        if digit > max_d1:
            max_d1 = digit
            max_d1_idx = i
    max_d2 = 0
    for i, digit in enumerate(bank[max_d1_idx + 1 :]):
        if digit > max_d2:
            max_d2 = digit

    joltage = int(str(max_d1) + str(max_d2))

    return joltage


def solve(data: list[list[int]]) -> int:
    total_joltage = 0
    for bank in data:
        total_joltage += get_joltage(bank)
    return total_joltage


if __name__ == "__main__":
    data = read_input("input.txt")
    print(solve(data))
