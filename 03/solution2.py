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


def find_max_idx(digits: list[int]) -> tuple[int, int]:
    max_d = 0
    max_d_idx = 0
    for i, digit in enumerate(digits):
        if digit > max_d:
            max_d = digit
            max_d_idx = i
    return max_d, max_d_idx


def get_joltage(bank: list[int]) -> int:
    joltage_digits = ""
    start_idx = 0

    for cutoff in range(len(bank) - 12, len(bank)):
        joltage_digit, joltage_digit_idx = find_max_idx(bank[start_idx : cutoff + 1])
        joltage_digits += str(joltage_digit)
        start_idx = start_idx + joltage_digit_idx + 1

    return int(joltage_digits)


def solve(data: list[list[int]]) -> int:
    total_joltage = 0
    for bank in data:
        total_joltage += get_joltage(bank)
    return total_joltage


if __name__ == "__main__":
    data = read_input("input.txt")
    print(solve(data))
