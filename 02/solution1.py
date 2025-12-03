def read_input(fpath: str) -> list[tuple[int, int]]:
    data = []
    with open(fpath, 'r') as f:
        lines = f.readlines()
        lines = lines[0].strip().split(',')
    for line in lines:
        start, end = line.split('-')
        data.append((int(start), int(end)))
    
    return data

def is_double(num: int):
    str_num = str(num)
    if len(str_num) % 2 != 0:
        return False

    mid_idx = len(str_num) // 2
    if str_num[:mid_idx] == str_num[mid_idx:]:
        return True
    return False


def solve(data: list[tuple[int, int]]):
    doubles = []
    for start, stop in data:
        for i in range(start, stop+1):
            if is_double(i):
                doubles.append(i)
    
    return sum(doubles)




if __name__ == '__main__':
    data = read_input('input.txt')
    print(solve(data))
